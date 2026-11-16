# ComicVision AI — Milestone 02 Consolidated Historical Evidence

Research date: 2026-11-15
Scope: CV0007–CV0020 (14 pending records)
Primary reference: Grand Comics Database (GCD) publicly indexed issue and series entries.

## Evidence policy

- **Historical match**: cited records support core bibliographic fields, but do **not** prove which edition/variant the user owns.
- **Cover date is not on-sale date**. Do not infer a cover-date month from an on-sale date.
- A qualified GCD date such as `[August] 1987` must remain qualified.
- This report does not change the CSV or authorize `verification_status=verified` without review of the project's verification requirements and physical evidence.

## Consolidated findings

| Comic ID | Issue | GCD date | US price | Evidence assessment |
|---|---|---|---|---|
| CV0007 | Captain America #282 | June 1983 | $0.60 | Core metadata matches; physical edition unresolved |
| CV0008 | Amazing Spider-Man Annual #14 | 1980 (month unspecified) | $0.75 | Keep issue_date blank; 1980-09-16 is *on-sale*, not confirmed cover month |
| CV0009 | ROM #53 | April 1984 | $0.60 | Core metadata matches; physical edition unresolved |
| CV0010 | Marvel Super-Heroes #83 | September 1979 | $0.40 | Core metadata matches; physical edition unresolved |
| CV0011 | Arak, Son of Thunder #29 | January 1984 | $0.75 | Core metadata matches; 1983 copyright/on-sale is not contradictory |
| CV0012 | Daredevil #237 | December 1986 | $0.75 | Core metadata matches; physical edition unresolved |
| CV0013 | Turok, Son of Stone #117 | September 1978 | $0.35 | Core metadata matches; Gold Key/Whitman variants |
| CV0014 | The New Humans #2 | [August] 1987 (qualified) | $1.95 | Preserve year 1987; leave month unresolved |
| CV0015 | Marvel Two-in-One #99 | May 1983 | $0.60 | Core metadata matches; physical edition unresolved |
| CV0016 | Fury of Firestorm #14 | July 1983 | $0.60 | Core metadata matches; GCD uses shorter series title |
| CV0017 | Turok, Son of Stone #118 | November 1978 | $0.35 | Core metadata matches; Gold Key/Whitman variants |
| CV0018 | Aliens vs. Predator: Duel #1 | March 1995 | $2.50 | Core metadata matches; physical edition unresolved |
| CV0019 | ROM #52 | March 1984 | $0.60 | Core metadata matches; physical edition unresolved |
| CV0020 | Dark Horse Classics: Aliens versus Predator #6 | July 1997 | $2.95 | Core metadata matches; physical edition unresolved |

## Traceable issue references

| ID | Source URL | Qualification / notes |
|---|---|---|
| CV0007 | https://www.comics.org/issue/37493/ | GCD Direct edition; other editions exist |
| CV0008 | https://www.comics.org/issue/33997/ | GCD Direct edition; 1980-09-16 is on-sale date |
| CV0009 | https://my.comics.org/issue/38572/ | GCD Direct edition |
| CV0010 | https://www.comics.org/issue/89054/ | GCD Direct edition |
| CV0011 | https://www.comics.org/issue/38160/ | GCD Direct edition; indicia title from #29 is Arak, Son of Thunder |
| CV0012 | https://www.comics.org/issue/42174/ | GCD Direct edition |
| CV0013 | https://www.comics.org/issue/304247/ | GCD Gold Key edition; Whitman variant exists |
| CV0014 | https://www.comics.org/issue/648648/ | GCD shows [August] 1987 and $1.95 US / $2.95 CA; co-published by Pied Piper Press Inc. and Campiti & Associates |
| CV0015 | https://www.comics.org/issue/37418/ | GCD Direct edition |
| CV0016 | https://www.comics.org/issue/853140/ | GCD Newsstand entry; series indexed The Fury of Firestorm |
| CV0017 | https://www.comics.org/issue/304248/ | GCD Gold Key edition; Whitman variant exists |
| CV0018 | https://my.comics.org/issue/212576/ | GCD Direct; $2.50 US / $3.50 CA |
| CV0019 | https://www.comics.org/issue/1090676/ | GCD Newsstand entry; Direct/Canadian variants exist |
| CV0020 | https://www.comics.org/issue/705596/ | GCD Direct; $2.95 US / $4.15 CA |

## Reconciliation and outstanding checks

1. **CV0008**: GCD records publication as 1980, not a known cover month. Preserve blank `issue_date` even though a Direct edition on-sale date is September 16, 1980.
2. **CV0014**: GCD date `[August] 1987` is qualified; preserve the qualification in the research log without populating an unqualified `issue_date`.
3. **CV0011**: January 1984 cover date can coexist with 1983 sales/copyright dates; do not conflate date types.
4. **CV0016**: GCD indexes the series as *The Fury of Firestorm*, while the catalog's longer title reflects the cover branding. Assess separately before normalization.
5. **CV0013 and CV0017**: GCD distinguishes Gold Key and Whitman editions; identify the physical copy before assigning an edition label.
6. **All records**: Historical issue-level evidence is now collected. Physical-cover correspondence and, where necessary, indicia or variant identification still require the dataset's verification gates before status changes.

## Proposed next action

Review this research report and incorporate evidence into the project's existing `reports/milestone_02_remaining_metadata_research.md` file. Then perform a single batch cover-evidence comparison, approve qualified core fields, and update the CSV in one controlled batch only after validation. Do not add an unqualified publication month to CV0008 or CV0014.
