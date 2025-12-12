# Flowchart Completeness Analysis: 55077 Lieferbeginn Process

## Overview
This document analyzes the flowchart you provided against the official MaCo API documentation to identify:
1. ✅ Correct scenarios
2. ⚠️ Incorrect/misleading scenarios  
3. ❌ Missing scenarios

---

## Flowchart Scenarios vs Documentation

### ✅ CORRECT Scenarios (Present in Flowchart)

#### 1. **55078 valid received** → Import → POST /updateProcessData 55078
**Status**: ✅ **CORRECT**  
**Documentation**: `PROCESS_GRAPH.json` → `success_erzeugend: "55078"`  
This is the standard success path for generating Marktlokation.

#### 2. **55080 received** → POST /updateProcessData 55080
**Status**: ✅ **CORRECT**  
**Documentation**: `PROCESS_GRAPH.json` → `rejection_erzeugend: "55080"`  
This is the standard rejection path for generating Marktlokation (e.g., wrong MaLo).

#### 3. **55036 Malo Prod already registered** → POST /updateProcessData 55036
**Status**: ✅ **CORRECT**  
**Documentation**: `PROCESS_GRAPH.json` → `info_existing_assignment: "55036"`  
NB informs about existing LFA assignment.

#### 4. **APERAK to 55077** → POST /updateProcessData APERAK Rejected 99999
**Status**: ✅ **CORRECT** (for technical errors)  
**Documentation**: APERAK is used for application-level/technical errors (malformed message, validation failures).  
**Note**: This is different from business rejections (55080). APERAK = technical error, 55080 = business rejection.

#### 5. **No feedback** → Cancel (55022) or Deadline (90000)
**Status**: ✅ **CORRECT**  
**Documentation**: `STORNIERUNG` process uses 55022 for cancellation requests.  
Timeout scenarios are valid edge cases.

---

### ⚠️ QUESTIONABLE/MISLEADING Scenarios

#### 1. **"55078 received but invalid"** → Decision → APERAK
**Status**: ⚠️ **CONCEPTUALLY WRONG**  
**Issue**: 
- **55078 is a SUCCESS response**, not a request that can be "invalid"
- If the MaLo is wrong in your 55077 request, you get **55080** (rejection), NOT 55078
- You cannot receive an "invalid 55078" - 55078 only comes if the request was successful

**What Should Happen**:
- Wrong MaLo in 55077 → **55080** (rejection)
- Technical/format error in 55077 → **APERAK**
- Valid 55077 → **55078** (success)

**Recommendation**: Remove this path or clarify it represents a different scenario (e.g., "55078 received but data quality issues detected").

---

### ❌ MISSING Scenarios

#### 1. **After 55036: Follow-up Flow**
**Status**: ❌ **MISSING**  
**What Should Be Shown**:
```
55036 received
  ↓
NB sends 55010 to LFA (you don't receive this)
  ↓
LFA responds: 55011 (accept) or 55012 (reject)
  ↓
If 55011: NB sends 55037 to LFA (termination)
  ↓
Then you receive: 55078 (success) OR 55080 (rejection)
```

**Documentation**: `PROCESS_GRAPH.json` → `LIEFERBEGINN.pruefis.anfrage_beendigung_lfa: ["55011", "55012"]`  
**Impact**: High - This is a critical flow when there's an existing supplier.

#### 2. **55037 (Beendigung Zuordnung LFA)**
**Status**: ❌ **MISSING**  
**When**: After 55036, if LFA accepts termination  
**Documentation**: `PROCESS_GRAPH.json` → `BEENDIGUNG_ZUORDNUNG_LFA.pruefis.notification: "55037"`  
**Note**: You (LFN) don't receive 55037 directly, but it's part of the process flow that leads to your 55078.

#### 3. **55038 (Aufhebung Zuordnung LFZ)**
**Status**: ❌ **MISSING**  
**When**: If there's a future supplier (LFZ) assignment that gets cancelled  
**Documentation**: `PROCESS_GRAPH.json` → `AUFHEBUNG_ZUORDNUNG_LFZ.pruefis.notification: "55038"`  
**Note**: You (LFN) don't receive this, but it's part of the process flow.

#### 4. **After 55078 Success: Follow-up Processes**
**Status**: ❌ **MISSING**  
**What Should Be Shown** (all triggered by NB after 55078):

**Immediate Follow-ups**:
- STAMMDATENAENDERUNG_NB (Prüfi: 55615, 55620, 55175, 55225, 55616, 55617, 55618, 55619, 55691)
- ABRECHNUNGSDATEN_BK (Prüfi: 55126) - **Always sent**
- ABRECHNUNGSDATEN_NN (Prüfi: 55218) - Only for consuming MaLo

**At Zuordnungsbeginn**:
- BERECHNUNGSFORMEL (Prüfi: 25001)
- EINRICHTUNG_KONFIG (Prüfi: 17134)
- ERSATZ_GRUNDVERSORGUNG (Prüfi: 55013) - If E/G required
- WIEDERHERSTELLUNG_ANSCHLUSS (Prüfi: 21040, 21039) - If blocked MaLo

**Documentation**: `PROCESS_GRAPH.json` → `LIEFERBEGINN.triggers_processes`  
**Impact**: High - These are mandatory follow-up processes.

#### 5. **Stornierung (55022) Response Messages**
**Status**: ❌ **MISSING**  
**What Should Be Shown**:
```
Send 55022 (Stornierung request)
  ↓
Receive: 55023 (Stornierung accepted) OR 55024 (Stornierung rejected)
```

**Documentation**: `PROCESS_GRAPH.json` → `STORNIERUNG.pruefis.response_success: "55023"`, `response_rejection: "55024"`  
**Impact**: Medium - Needed for cancellation flow.

---

## Complete Flow After Sending 55077

Based on documentation, here's what **can** happen:

### Direct Responses (to your 55077 request):

1. **55078** (Success) ✅
   - Then follow-up processes (see above)

2. **55080** (Rejection) ✅
   - Wrong MaLo, validation failures, etc.
   - Contains `freitext` with rejection reason

3. **55036** (Info existing assignment) ✅
   - Then follow-up flow (55010 → 55011/55012 → 55037 → 55078/55080)

4. **APERAK** (Technical error) ✅
   - Malformed message, format errors, etc.

5. **No response** (Timeout) ✅
   - Deadline passed (90000)
   - Can retry or cancel

### After 55036 (Missing from Flowchart):

6. **55078 or 55080** (Final outcome after LFA termination)
   - After NB processes LFA termination (55037)
   - You receive final success or rejection

### After 55078 Success (Missing from Flowchart):

7. **Multiple follow-up processes** (see list above)
   - Immediate: STAMMDATENAENDERUNG_NB, ABRECHNUNGSDATEN_BK, ABRECHNUNGSDATEN_NN
   - At Zuordnungsbeginn: BERECHNUNGSFORMEL, EINRICHTUNG_KONFIG, etc.

### Cancellation Flow (Partially Missing):

8. **55022** (Stornierung request) ✅
9. **55023** (Stornierung accepted) ❌ Missing
10. **55024** (Stornierung rejected) ❌ Missing

---

## Summary: Completeness Assessment

### ✅ Covered Correctly (5 scenarios):
- 55078 success
- 55080 rejection  
- 55036 info
- APERAK technical error
- No feedback/timeout

### ⚠️ Incorrect/Misleading (1 scenario):
- "55078 received but invalid" - This path is conceptually wrong

### ❌ Missing Critical Scenarios (3+ categories):
1. **After 55036 flow** - Complete follow-up sequence missing
2. **After 55078 success** - All follow-up processes missing
3. **Stornierung responses** - 55023/55024 missing

---

## Recommendations

### 1. Fix the "55078 invalid" Path
**Current**: "55078 received but invalid" → APERAK  
**Should Be**: Remove this path OR clarify it's for data quality issues, not wrong MaLo  
**Correct Flow**: Wrong MaLo → 55080 (not 55078)

### 2. Add After-55036 Flow
```
55036 → Wait → 55078 (success) OR 55080 (rejection)
```
Show that 55036 is intermediate, not final.

### 3. Add Follow-up Processes After 55078
Show that after 55078 success, multiple follow-up messages arrive:
- Immediate follow-ups
- Follow-ups at Zuordnungsbeginn

### 4. Add Stornierung Response Handling
```
55022 sent → 55023 (accepted) OR 55024 (rejected)
```

### 5. Clarify APERAK vs 55080
- **APERAK** = Technical/application-level error (format, validation)
- **55080** = Business-level rejection (wrong MaLo, business rules)

---

## Answer to Your Question

**"Are these cases complete?"**

**No, the flowchart is NOT complete.** It's missing:

1. **The follow-up flow after 55036** (critical for supplier switches)
2. **All follow-up processes after 55078 success** (mandatory processes)
3. **Stornierung response messages** (55023/55024)
4. **The "55078 invalid" path is conceptually wrong** - should be 55080 for wrong MaLo

The flowchart covers the **initial responses** well, but misses the **subsequent process flows** that are part of the complete Lieferbeginn process.

---

*Analysis based on: PROCESS_GRAPH.json, LIEFERBEGINN_PROCESS_MAP.md, and official MaCo API documentation*
