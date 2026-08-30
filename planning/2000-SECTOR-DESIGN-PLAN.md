# Sector Design Plan

This is a structural catalog plan. It does not contain authored designs or sector research.

The catalog was originally planned as 2,000 studies across twenty core sections per sector.
It has since been extended by seven universal roles per sector, giving 2,700 planned studies.
The file name records the original core figure and is kept for continuity.

| # | Sector | Directory | Prefix | Sections | Studies / Section | Studies / Sector | Status |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| 01 | Healthcare & Medical Clinics | `healthcare-medical/` | HC | 27 | 5 | 135 | NOT_STARTED |
| 02 | Dental Clinics | `dental-clinics/` | DN | 27 | 5 | 135 | NOT_STARTED |
| 03 | Law Firms | `law-firms/` | LAW | 27 | 5 | 135 | NOT_STARTED |
| 04 | Finance, Accounting & Insurance | `finance-accounting-insurance/` | FIN | 27 | 5 | 135 | NOT_STARTED |
| 05 | Real Estate | `real-estate/` | RE | 27 | 5 | 135 | NOT_STARTED |
| 06 | Construction & Contractors | `construction-contractors/` | CON | 27 | 5 | 135 | NOT_STARTED |
| 07 | Architecture & Interior Design | `architecture-interior-design/` | ARC | 27 | 5 | 135 | NOT_STARTED |
| 08 | Manufacturing & Industrial | `manufacturing-industrial/` | MFG | 27 | 5 | 135 | NOT_STARTED |
| 09 | Logistics & Transportation | `logistics-transportation/` | LOG | 27 | 5 | 135 | NOT_STARTED |
| 10 | Automotive | `automotive/` | AUTO | 27 | 5 | 135 | NOT_STARTED |
| 11 | Hotels & Hospitality | `hotels-hospitality/` | HOT | 27 | 5 | 135 | NOT_STARTED |
| 12 | Restaurants & Food Service | `restaurants-food-service/` | REST | 27 | 5 | 135 | NOT_STARTED |
| 13 | Beauty, Wellness & Spa | `beauty-wellness-spa/` | WELL | 27 | 5 | 135 | NOT_STARTED |
| 14 | Education & Training | `education-training/` | EDU | 27 | 5 | 135 | NOT_STARTED |
| 15 | SaaS & Software | `saas-software/` | SAAS | 27 | 5 | 135 | NOT_STARTED |
| 16 | IT, Cybersecurity & Managed Services | `it-cybersecurity-managed-services/` | IT | 27 | 5 | 135 | NOT_STARTED |
| 17 | Consulting & B2B Professional Services | `consulting-b2b-professional-services/` | CONS | 27 | 5 | 135 | NOT_STARTED |
| 18 | Energy, Solar & Engineering | `energy-solar-engineering/` | ENG | 27 | 5 | 135 | NOT_STARTED |
| 19 | Home Services | `home-services/` | HOME | 27 | 5 | 135 | NOT_STARTED |
| 20 | Retail & E-commerce | `retail-ecommerce/` | RET | 27 | 5 | 135 | NOT_STARTED |
| **Total** | **20 sectors** |  | **20 unique prefixes** | **540** | **5** | **2,700** | **IN_PROGRESS** |

## Section Model

| Range | Model | Sections per sector | Scaffolded |
| --- | --- | ---: | --- |
| S01–S20 | Sector Core — roles specific to the sector | 20 | Yes |
| S21–S27 | Universal Extended Site Architecture — detail-page and page-context roles shared by every sector | 7 | Yes |
| S28+ | Reserved for future sector-native page types | — | No, deliberately not created |

The seven extended roles are the same in every sector. Their numbers and IDs are canonical;
only the sector-facing section name adapts to the sector's own terminology.

| Section | Universal Role |
| --- | --- |
| S21 | Subpage Hero |
| S22 | Breadcrumb / Context Navigation |
| S23 | Service / Offering Detail |
| S24 | Project / Case Study Detail |
| S25 | Article / Insight Detail |
| S26 | Person / Profile Detail |
| S27 | Location / Branch Detail |

Where a role has reduced applicability to a sector, the limitation is documented in that
sector's brief and section README rather than the role being dropped. A documented limitation
is useful research information; a missing role is not.

## Catalog Formula

    Core catalog       20 sectors × 20 core sections     × 5 studies = 2,000 planned studies
    Extended catalog   20 sectors ×  7 extended sections × 5 studies =   700 planned studies
    Total catalog      20 sectors × 27 sections          × 5 studies = 2,700 planned studies

The original core catalog of 2,000 studies is unchanged; the 700 extended studies are added to
it. The five default study territories are documented in standards/01-AUTHORING-STANDARD.md.
Stable ID rules are documented in standards/02-NAMING-AND-ID-STANDARD.md.
