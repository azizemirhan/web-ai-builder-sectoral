# Section ID

WELL-S19

# Section Name

Contact

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S19-001
WELL-S19-002
WELL-S19-003
WELL-S19-004
WELL-S19-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S19-001` | Universal / Safe |
| `WELL-S19-002` | Premium / Editorial |
| `WELL-S19-003` | Structured / Visual Modular |
| `WELL-S19-004` | Conversion-led |
| `WELL-S19-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

How to reach a person, which way of reaching them suits what, and what happens after you make
contact.

It answers: *if I have a question rather than a booking, who do I speak to and what will happen?*

# The Governing Constraint — Every Detail Is Reserved, So The Section Is Made Of Policy

A contact section is almost entirely made of data a placeholder cannot know. Applying the `S11`
field-versus-figure test — *reserve the field when the empty field asserts nothing; omit it when the
empty field asserts a system* — gives:

| Element | Treatment |
| --- | --- |
| Phone number | **Reserved field** — every studio has one |
| Email address | **Reserved field** |
| Postal address | **Reserved field**, and only where a study needs it — the set of locations is `S16` |
| Opening hours | **Omitted** — an empty hours table asserts a weekly schedule and prints figures |
| Response time | **Omitted** — *"we reply within —"* is an invented figure and a service promise |
| A map | **Omitted here.** `S16` already established that a map is a reserved area and never an embed; repeating it in `S19` would blur the boundary |
| Social handles | **Omitted** — an invented account name is an invented identity |
| Live chat | **Omitted** — mocking a chat widget invents a staffed channel |

**So the section cannot be built out of its own contact details.** What is left is the part most
contact sections leave out, and it is entirely authorable because it is operating policy rather than
a claim:

1. **What each channel is actually for.** The phone for *will this suit me* and *can you fit me in*;
   writing for anything with a list or a photo in it; coming in for when you want to see the room
   before you commit.
2. **A message is not a booking.** Nothing is held until somebody replies. This is the section's
   most valuable sentence — it costs the studio nothing, it prevents the single most common
   misunderstanding, and it is exactly the kind of thing a placeholder can say honestly. It appears
   in **every study in this batch**, on the `S17` pattern where the strongest content was the
   awkward bit nobody prints.
3. **Who replies.** The person who would be doing the treatment, not a shared inbox.
4. **What will not be answered in writing.** Whether a treatment suits one particular person is a
   conversation, not an email — and if it is about something changing on your skin, it is a
   doctor's question. Stated in one line only; the full version of that position belongs to `S15`
   and `S18`.

**Not present in any study:** an invented telephone number, email address, street address, postcode,
set of opening hours, response time, staff name, social handle or account; a map, an embed, a live
chat widget or a chat-availability indicator; a response-rate or satisfaction figure; an urgency
device; a newsletter capture.

# Boundary With S06, S16 And S20

| Section | What it owns |
| --- | --- |
| `S06` Consultation Booking | **Booking a consultation** — the flow, and what happens at one |
| `S16` Locations | **Which studios exist and where** — the set, with the reserved map area |
| `S19` Contact | **How to reach a person**, which channel suits what, and what follows |
| `S20` Final Booking CTA | **The closing ask** at the foot of the page |
| `S27` Location Detail | **One branch in full**, with its own details |

    Choosing a time is S06. Choosing a building is S16.
    Asking a question before you are ready to do either is S19.

The form in `S19-004` is a **message** form — a name, a way to reply, and what you want to ask. It
has no treatment picker, no date and no time, because the moment it acquires those it has become
`S06` in the wrong place.

# Out Of Scope

- A global site header, primary navigation or footer
- A booking flow, an appointment picker or a treatment selector, which belong to S06
- The set of locations and any map, which belong to S16
- One branch in full, which belongs to S27
- Opening hours, response times and any other figure
- Medical or diagnostic content

# Authoring Questions

**1. What is the primary visual element of this role?**

There is not an obvious one, and that is the design problem. A contact section normally leans on a
map or a photograph of the building; both belong to `S16`. So each study has to decide what carries
the composition when the details are reserved and the map is gone — the channels themselves, a
single sentence, a form, or the phone number treated as an object.

**2. What must a visitor understand immediately?**

Which way of getting in touch suits their question, and that writing in does not hold anything.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
