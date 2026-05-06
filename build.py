"""Generate static HTML for virtual clinic concept sites.

Run: python3 build.py
Outputs: index.html and one folder per clinic with its own index.html.
"""
import html
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
SITE_NAME = "Virtual Clinics"
SITE_TAGLINE = "Concept sites for sixteen specialty virtual care programs."
REPO_BASE = "/virtual-clinics"  # GitHub Pages base path for project repo

CLINICS = [
    {
        "slug": "pelvic-floor-pt",
        "name": "Pelvic Floor Physical Therapy",
        "short": "Pelvic Floor PT",
        "tagline": "Specialized virtual physical therapy for pelvic floor dysfunction.",
        "accent": "#0d8b8b",
        "accent_soft": "#e6f4f4",
        "category": "Physical Therapy",
        "intro": (
            "Pelvic floor conditions are common, treatable, and often under-addressed. "
            "Our program connects you with pelvic-health-certified physical therapists "
            "who design individualized programs you complete at home — with the same "
            "clinical rigor as in-person care, without the waiting rooms."
        ),
        "conditions": [
            "Urinary urgency, frequency, and leakage",
            "Postpartum recovery and diastasis recti",
            "Pelvic organ prolapse (mild to moderate)",
            "Pelvic pain, vulvodynia, and dyspareunia",
            "Endometriosis-related pelvic pain",
            "Pre- and post-surgical pelvic rehabilitation",
            "Constipation and bowel dysfunction",
        ],
        "approach_intro": (
            "Pelvic floor PT is highly specialized. Our clinicians have post-graduate "
            "certification in pelvic health (CAPP-Pelvic, PRPC, or equivalent) and "
            "build programs around three pillars:"
        ),
        "pillars": [
            ("Assessment", "A thorough video evaluation covering history, symptom mapping, posture, breathing patterns, and functional movement."),
            ("Education", "Understanding why your pelvic floor is behaving the way it is — often the most therapeutic part of treatment."),
            ("Targeted exercise", "A progressive home program combining motor control, mobility, strength, and behavioral retraining."),
        ],
        "steps": [
            ("Free 15-minute consult", "We learn about your symptoms and confirm whether virtual pelvic PT is the right fit."),
            ("60-minute initial evaluation", "Comprehensive video assessment with your dedicated PT. You leave with a written plan."),
            ("Weekly follow-ups", "30-minute sessions to progress your program, troubleshoot, and answer questions."),
            ("Discharge and maintenance", "Most patients see meaningful improvement in 8–12 weeks and graduate to independent maintenance."),
        ],
        "best_for": [
            "Adults with persistent pelvic floor symptoms",
            "Those who prefer the privacy of home-based care",
            "Patients without local access to a pelvic PT",
            "Postpartum patients past their 6-week clearance",
        ],
        "not_for": [
            "Acute pelvic infections requiring urgent care",
            "Severe prolapse needing surgical evaluation",
            "Patients who require internal manual therapy as primary treatment",
        ],
        "faq": [
            ("Can pelvic floor PT really work without an in-person internal exam?",
             "For most patients, yes. A thorough external evaluation, symptom history, and functional testing provide enough information to build an effective program. We refer for internal assessment when clinically indicated."),
            ("Do I need any equipment?",
             "Most programs use a yoga mat and a few household items. In specific cases we recommend a biofeedback device or pelvic wand, which we discuss with you."),
            ("Is this covered by insurance?",
             "We are a cash-pay practice and provide superbills for out-of-network reimbursement. Many patients receive partial reimbursement."),
            ("How long until I see results?",
             "Most patients notice meaningful changes within 4–6 weeks, with substantial improvement by 8–12 weeks."),
        ],
    },
    {
        "slug": "tinnitus-retraining",
        "name": "Tinnitus Retraining Therapy",
        "short": "Tinnitus Retraining",
        "tagline": "An evidence-based program to habituate the brain to chronic tinnitus.",
        "accent": "#1e4a8a",
        "accent_soft": "#e7edf7",
        "category": "Audiology & Neuro-otology",
        "intro": (
            "Tinnitus Retraining Therapy (TRT) is a structured, long-term program that "
            "combines directive counseling with sound therapy to retrain how your brain "
            "processes tinnitus. Most patients reach meaningful habituation in 12–24 months."
        ),
        "conditions": [
            "Chronic subjective tinnitus",
            "Hyperacusis and sound sensitivity",
            "Tinnitus-related insomnia",
            "Tinnitus-related anxiety and avoidance",
            "Misophonia (specific protocols)",
        ],
        "approach_intro": (
            "TRT is not a quick fix. It is a neuroscience-grounded program built on the "
            "Jastreboff model of tinnitus, delivered by audiologists with formal TRT training:"
        ),
        "pillars": [
            ("Directive counseling", "Structured education about tinnitus neurophysiology that reduces the threat response driving symptom severity."),
            ("Sound therapy", "Personalized low-level broadband sound enrichment to weaken the contrast between tinnitus and silence."),
            ("Long-term tracking", "Quarterly outcome measures (THI, VAS) to confirm habituation is on track."),
        ],
        "steps": [
            ("Initial intake", "Hearing history, audiogram review, and TRT category assignment."),
            ("Counseling phase", "Two to four structured counseling sessions over the first month."),
            ("Sound therapy onboarding", "Recommendations for sound generators, hearing aids with masking, or environmental sound."),
            ("Quarterly check-ins", "Brief sessions every three months for 18–24 months."),
        ],
        "best_for": [
            "Patients with bothersome tinnitus persisting beyond 6 months",
            "Those willing to commit to a multi-year program",
            "Patients who have already had ENT clearance",
        ],
        "not_for": [
            "New-onset tinnitus (under 3 months) without ENT evaluation",
            "Pulsatile tinnitus without vascular workup",
            "Acute Meniere's flares or sudden hearing loss",
        ],
        "faq": [
            ("Will TRT make my tinnitus go away?",
             "TRT is about habituation, not elimination. The goal is for tinnitus to fade into the background — present but no longer distressing or noticed most of the day."),
            ("Do I need to wear sound generators all day?",
             "During the active phase, most protocols recommend 6–8 hours per day of low-level sound enrichment. This tapers as habituation progresses."),
            ("Is TRT the same as CBT for tinnitus?",
             "They are different evidence-based approaches. TRT emphasizes counseling and sound therapy together. CBT focuses on cognitive and behavioral patterns. Some patients benefit from both."),
            ("Can I do TRT entirely online?",
             "Yes. Counseling, outcome tracking, and sound therapy guidance translate well to telehealth. We coordinate with local audiologists for any in-person fittings needed."),
        ],
    },
    {
        "slug": "speech-therapy",
        "name": "Speech Therapy",
        "short": "Speech Therapy",
        "tagline": "Virtual speech-language pathology for adults and children.",
        "accent": "#d35a4a",
        "accent_soft": "#fbe9e6",
        "category": "Speech-Language Pathology",
        "intro": (
            "Our speech-language pathologists deliver evidence-based therapy for "
            "communication, voice, and swallowing concerns across the lifespan — "
            "from preschool articulation to post-stroke aphasia recovery."
        ),
        "conditions": [
            "Childhood-onset stuttering (preschool through adolescent)",
            "Adult stuttering and avoidance-reduction therapy",
            "Cluttering",
            "Childhood apraxia of speech (CAS)",
            "Articulation disorders, including persistent /r/, /s/, and /l/ errors",
            "Phonological process disorders",
            "Muscle tension dysphonia and other functional voice disorders",
            "Vocal nodules, polyps, and lesion-related voice changes (with ENT)",
            "Chronic cough and paradoxical vocal fold movement",
            "Post-stroke aphasia (Broca's, Wernicke's, anomic, conduction)",
            "Acquired apraxia of speech",
            "Cognitive-communication after TBI or concussion",
            "Right-hemisphere communication disorder",
            "Social and pragmatic communication support",
            "Gender-affirming voice",
            "Accent modification",
            "Professional and performance voice coaching",
        ],
        "condition_details": [
            ("Stuttering and fluency disorders",
             "Stuttering is one of the most common reasons people reach out to us, and the right approach depends heavily on age and goals. For preschoolers we use the Lidcombe Program — a parent-delivered, evidence-based approach with strong long-term outcomes when started early. For school-age children, adolescents, and adults we draw on the Camperdown Program, stuttering modification (Van Riper), and avoidance-reduction therapy (ARTS). Adult work often emphasizes the affective and avoidance dimensions of stuttering as much as speech mechanics, because that is usually where real-world function lives. We also treat cluttering, which is frequently misidentified as stuttering and requires a distinct approach centered on rate and clarity."),
            ("Voice disorders",
             "We treat the full range of functional voice problems: muscle tension dysphonia, vocal fatigue, chronic hoarseness, vocal nodules and polyps (in coordination with your ENT or laryngologist), vocal cord paresis, chronic cough, and paradoxical vocal fold movement. Voice work translates well to telehealth — we can hear changes clearly over a good microphone and our clinicians use stroboscopy reports from your ENT alongside their own perceptual assessment. For singers and professional voice users, we coordinate with laryngologists and singing teachers as part of a team."),
            ("Adult acquired neuro-recovery",
             "After a stroke or brain injury, we work on aphasia, apraxia of speech, and cognitive-communication concerns. Depending on the profile, our therapists draw on Semantic Feature Analysis, Verb Network Strengthening Treatment (VNeST), script training, Constraint-Induced Aphasia Therapy adaptations, and sentence-level approaches like Treatment of Underlying Forms. For cognitive-communication after TBI or concussion, we focus on attention, executive function, and the social-pragmatic skills that often get hit hardest."),
            ("Pediatric speech sound disorders",
             "We distinguish carefully between articulation disorders (specific sound errors), phonological process disorders (pattern-based errors), and childhood apraxia of speech — because the treatment approach is different for each. For CAS, we use Dynamic Temporal and Tactile Cueing (DTTC) and similar motor-based approaches. For phonological disorders, cycles or minimal pairs. Persistent /r/ and /s/ errors in older children and teens are a particular focus, since these are often missed in school therapy."),
            ("Social and pragmatic communication",
             "We support social communication for autistic adults and adolescents using a neurodiversity-affirming framework — meaning the goal is communication that works for the client in their own world, not masking or compliance with neurotypical norms. We also help adults with ADHD-related executive-communication challenges, and provide structured pragmatic language work for school-age children when that is what fits the family's goals."),
            ("Gender-affirming voice and elective work",
             "Gender-affirming voice therapy targets pitch, resonance, intonation, articulation, and nonverbal communication — with an emphasis on vocal health and durability of changes. We coordinate with laryngologists when surgical options are being considered. We also offer accent modification and professional voice coaching for clients whose careers involve sustained voice use, presenting, or performing."),
        ],
        "approach_intro": (
            "We match each patient with an SLP whose specialty fits their needs. "
            "Programs are individualized, outcome-tracked, and family-involved when relevant:"
        ),
        "pillars": [
            ("Standardized evaluation", "Validated assessments delivered over telehealth with adapted protocols where needed."),
            ("Skill-based therapy", "Targeted, repetition-based practice using teletherapy-optimized activities."),
            ("Carryover", "Home practice plans, family training, and real-world generalization between sessions."),
        ],
        "steps": [
            ("Screening call", "We confirm clinical fit and match you with a specialized SLP."),
            ("Evaluation", "60–90 minute initial assessment with a written report."),
            ("Therapy sessions", "Typically once or twice weekly, 30–45 minutes each."),
            ("Re-evaluation", "Every 12 weeks to measure progress and adjust the plan."),
        ],
        "best_for": [
            "Patients comfortable with screen-based interaction",
            "Families seeking specialized SLPs not locally available",
            "Adults wanting flexible, work-friendly scheduling",
        ],
        "not_for": [
            "Severe dysphagia requiring instrumental swallow studies",
            "Children whose attention to screens is below treatment threshold",
            "Acute medical settings",
        ],
        "faq": [
            ("Does telehealth speech therapy actually work?",
             "Research over the past decade — including for pediatric articulation, aphasia, and voice — consistently shows comparable outcomes to in-person care for most diagnoses."),
            ("How young can my child start?",
             "We typically begin around age 3, depending on attention and screen tolerance. We coach parents directly for younger children."),
            ("Will insurance cover this?",
             "We are out of network and provide superbills. Many plans reimburse a meaningful portion of session costs."),
            ("Can adults benefit from speech therapy?",
             "Absolutely. Voice issues, post-stroke recovery, executive-communication concerns, and stuttering all respond to skilled adult-focused therapy."),
        ],
    },
    {
        "slug": "nicotine-cessation",
        "name": "Nicotine and Vaping Cessation",
        "short": "Nicotine Cessation",
        "tagline": "A 12-week combined CBT and varenicline program for quitting nicotine.",
        "accent": "#2e7d4a",
        "accent_soft": "#e7f2ec",
        "category": "Behavioral Health & Medication",
        "intro": (
            "Combining medication with behavioral support roughly doubles quit rates "
            "compared to either alone. Our program pairs a prescriber managing varenicline "
            "(Chantix) with a CBT therapist over a structured 12-week course."
        ),
        "conditions": [
            "Cigarette smoking",
            "E-cigarette and vape dependence",
            "Smokeless tobacco and pouches",
            "Polysubstance nicotine use",
            "Relapse after prior quit attempts",
        ],
        "approach_intro": (
            "Quitting nicotine is hard because the drug rewires reward, attention, and "
            "stress circuits. We treat both the neurobiology and the behavior:"
        ),
        "pillars": [
            ("Medical management", "Prescriber-led varenicline titration, including the flexible-quit protocol that lets you set a quit date 1–5 weeks after starting."),
            ("CBT skills", "Weekly therapy targeting triggers, urges, identity, and relapse prevention."),
            ("Tracking", "Daily check-ins via app, with carbon monoxide self-tests for cigarette users who want objective feedback."),
        ],
        "steps": [
            ("Intake", "Medical and behavioral assessment with both providers in the first week."),
            ("Lead-in (weeks 1–2)", "Start varenicline, begin CBT, set a quit date."),
            ("Quit and stabilize (weeks 3–8)", "Active quitting with weekly therapy and prescriber check-ins."),
            ("Maintenance (weeks 9–12)", "Relapse-prevention skills and medication taper planning."),
        ],
        "best_for": [
            "Adults motivated to quit within the next month",
            "Those who have tried and relapsed in the past",
            "Heavy daily users (>10 cigarettes/day or all-day vape use)",
        ],
        "not_for": [
            "Patients with active suicidal ideation (varenicline contraindication review needed)",
            "Pregnant patients (we refer to specialized programs)",
            "Severe untreated psychiatric illness without existing care team",
        ],
        "faq": [
            ("Why varenicline and not nicotine replacement?",
             "Varenicline has the strongest evidence base of any single agent for tobacco cessation. Some patients combine it with NRT under prescriber guidance."),
            ("What about the old varenicline warnings?",
             "The FDA black box warning on neuropsychiatric effects was removed in 2016 after the EAGLES trial showed no significant excess risk. We still screen carefully."),
            ("Does this work for vaping?",
             "Yes. The combination of CBT and varenicline is increasingly used for vape cessation, with growing evidence of effectiveness."),
            ("What if I relapse?",
             "Relapse is part of most successful quit journeys. Our program treats it as data, not failure, and adjusts the plan."),
        ],
    },
    {
        "slug": "benzo-tapering",
        "name": "Benzodiazepine Tapering",
        "short": "Benzo Tapering",
        "tagline": "Slow, supervised tapering for benzodiazepine dependence.",
        "accent": "#5a6c7d",
        "accent_soft": "#eaedf0",
        "category": "Psychiatry & Addiction Medicine",
        "intro": (
            "Long-term benzodiazepine use can produce physical dependence even at "
            "prescribed doses. Coming off requires patience, expertise, and support. "
            "Our clinicians follow Ashton-style tapering with modern adjustments — "
            "typically over 6–24 months, paced by symptoms rather than the calendar."
        ),
        "conditions": [
            "Long-term benzodiazepine prescription dependence",
            "BIND (benzodiazepine-induced neurological dysfunction) symptoms",
            "Z-drug (zolpidem, eszopiclone) tapering",
            "Inter-dose withdrawal and tolerance",
            "Post-acute withdrawal symptoms (PAWS)",
        ],
        "approach_intro": (
            "Tapering is not a competition. The goal is a steady, sustainable reduction "
            "that you can complete without traumatic withdrawal:"
        ),
        "pillars": [
            ("Crossover when needed", "Switching to a long-half-life agent (typically diazepam) for steadier blood levels."),
            ("Micro-tapering", "Reductions of 5–10% every 2–4 weeks, often using compounded liquid or split tablets."),
            ("Supportive care", "Sleep, nervous system regulation, nutrition, and (when appropriate) adjunct medications."),
        ],
        "steps": [
            ("Comprehensive intake", "Medication history, prior taper attempts, and current symptoms."),
            ("Plan design", "A written taper schedule co-created with you, with clear flexibility built in."),
            ("Active taper", "Bi-weekly visits during reductions, with messaging access for symptom support."),
            ("Post-taper recovery", "Months of monitoring and PAWS support after the last dose."),
        ],
        "best_for": [
            "Patients on stable benzodiazepine doses for over 6 months",
            "Those who have tried to taper before and run into severe withdrawal",
            "Patients whose prescriber is unable to support a slow taper",
        ],
        "not_for": [
            "Active polysubstance use disorder requiring inpatient care",
            "Patients in acute medical crisis",
            "Those seeking rapid detox (we do not offer this)",
        ],
        "faq": [
            ("How slow is your taper?",
             "Most patients reduce by 5–10% of their current dose every 2–4 weeks. The exact pace is set by symptoms, not a fixed schedule."),
            ("Will I have withdrawal?",
             "A well-paced taper minimizes withdrawal. Some symptoms are common but should remain tolerable. We adjust if they don't."),
            ("What about Klonopin or Xanax — do I have to switch to Valium?",
             "Not always. Crossover helps when shorter-acting agents cause inter-dose withdrawal, but some patients taper directly from their current medication."),
            ("Do you prescribe other medications during the taper?",
             "When clinically appropriate, we may use adjuncts (e.g., gabapentinoids, certain antihistamines, propranolol) to ease specific symptoms — never another sedative-hypnotic class as a substitute."),
        ],
    },
    {
        "slug": "chronic-pain",
        "name": "Chronic Pain Program",
        "short": "Chronic Pain",
        "tagline": "Multimodal, non-opioid-centered care for persistent pain.",
        "accent": "#6b3fa0",
        "accent_soft": "#efe9f6",
        "category": "Pain Medicine & Psychology",
        "intro": (
            "Chronic pain rarely responds to a single intervention. Our program brings "
            "together pain psychology, movement specialists, and medical management to "
            "address the neurobiological, behavioral, and physical drivers of persistent pain."
        ),
        "conditions": [
            "Chronic low back and neck pain",
            "Fibromyalgia and widespread pain",
            "Headache and migraine (chronic)",
            "Neuropathic pain syndromes",
            "Post-surgical persistent pain",
            "Pelvic pain and CRPS (with appropriate workup)",
        ],
        "approach_intro": (
            "We use evidence-based modalities that target the central nervous system's "
            "role in chronic pain, alongside thoughtful medical care:"
        ),
        "pillars": [
            ("Pain psychology", "PRT, EAET, ACT, and CBT delivered by therapists trained specifically in chronic pain."),
            ("Movement re-education", "Graded exposure, paced activity, and gentle movement programs with PT consultation."),
            ("Medication strategy", "Rational use of non-opioid agents — SNRIs, gabapentinoids, low-dose naltrexone, topicals — when indicated."),
        ],
        "steps": [
            ("Comprehensive intake", "90-minute biopsychosocial evaluation."),
            ("Personalized plan", "A written plan combining the modalities most likely to help your specific pain pattern."),
            ("Active phase", "Weekly therapy and biweekly medical visits over 12–16 weeks."),
            ("Maintenance", "Monthly check-ins as you build independence with your skills."),
        ],
        "best_for": [
            "Adults with pain persisting beyond 3 months",
            "Patients tired of single-discipline approaches",
            "Those open to addressing the brain-body connection in pain",
        ],
        "not_for": [
            "Acute injury or undiagnosed pain requiring imaging or specialty workup",
            "Patients seeking opioid prescriptions (we do not prescribe long-term opioids)",
            "Pain due to active malignancy",
        ],
        "faq": [
            ("Do you say my pain is 'in my head'?",
             "No. All pain is real. We treat the neurobiology of chronic pain — which includes the brain — without dismissing your physical experience."),
            ("What is PRT?",
             "Pain Reprocessing Therapy is a recent evidence-based approach for nociplastic pain, helping patients reframe pain signals their brain is generating in the absence of ongoing tissue damage."),
            ("Do you prescribe medications?",
             "Yes — non-opioid agents when clinically appropriate. We coordinate with your other prescribers."),
            ("How long is the program?",
             "Most patients engage actively for 4–6 months, then transition to lighter maintenance."),
        ],
    },
    {
        "slug": "hand-therapy",
        "name": "Hand Therapy",
        "short": "Hand Therapy",
        "tagline": "Virtual care from certified hand therapists for hand, wrist, and elbow conditions.",
        "accent": "#c47a1f",
        "accent_soft": "#f8efe1",
        "category": "Occupational & Hand Therapy",
        "intro": (
            "Certified Hand Therapists (CHTs) are OTs and PTs with thousands of hours "
            "of advanced training in upper-extremity rehab. Our virtual program brings "
            "this specialty care to patients without local access."
        ),
        "conditions": [
            "Thumb CMC and finger osteoarthritis",
            "Carpal tunnel syndrome",
            "Trigger finger and trigger thumb",
            "De Quervain tenosynovitis",
            "Tennis and golfer's elbow",
            "Post-fracture and post-surgical rehab",
            "Dupuytren's contracture (non-surgical)",
        ],
        "approach_intro": (
            "Hand therapy combines movement, tissue work, splinting, and ergonomic "
            "redesign. Virtual care can deliver most of this directly:"
        ),
        "pillars": [
            ("Targeted exercise", "Tendon glides, nerve glides, joint mobility, and grip programs progressed over time."),
            ("Splinting guidance", "We measure remotely and ship custom-fit orthoses or recommend specific over-the-counter options."),
            ("Activity modification", "Real-time review of how you use your hands at work and home — often the most impactful change."),
        ],
        "steps": [
            ("Initial visit", "60-minute video evaluation with a CHT, including movement and functional testing."),
            ("Equipment setup", "We arrange any splints, exercise tools, or measurement aids by mail."),
            ("Therapy sessions", "Weekly 30-minute follow-ups, typically for 6–12 weeks."),
            ("Discharge", "Independent maintenance program with optional check-ins."),
        ],
        "best_for": [
            "Adults with non-acute hand or arm conditions",
            "Post-op patients past the early splinting phase",
            "Patients without a local CHT",
        ],
        "not_for": [
            "Acute fractures requiring in-person casting",
            "Conditions requiring continuous in-person manual therapy",
            "Severe wound care needs",
        ],
        "faq": [
            ("Can a hand therapist really evaluate me over video?",
             "Yes — for most conditions. CHTs use guided self-assessment, functional tasks, and goniometry techniques adapted for telehealth."),
            ("What about splints?",
             "We can ship pre-fabricated splints sized from your measurements, or coordinate custom thermoplastic splints with a local provider."),
            ("Will this help arthritis?",
             "Hand therapy doesn't reverse arthritis but consistently improves function, pain, and grip strength — particularly for thumb CMC OA."),
            ("Is this covered by insurance?",
             "We are out-of-network and provide superbills. Many plans reimburse a portion of OT/PT services."),
        ],
    },
    {
        "slug": "kidney-stone-nutrition",
        "name": "Kidney Stone Nutrition",
        "short": "Kidney Stone Nutrition",
        "tagline": "Specialized dietetics for preventing recurrent kidney stones.",
        "accent": "#b8552d",
        "accent_soft": "#f6e6dd",
        "category": "Medical Nutrition Therapy",
        "intro": (
            "Most people who form one kidney stone form another. Diet is one of the "
            "few levers patients can actually pull — but generic 'low-oxalate' advice "
            "often misses the point. Our registered dietitians interpret your 24-hour "
            "urine results and design a stone-specific prevention plan."
        ),
        "conditions": [
            "Recurrent calcium oxalate stones",
            "Calcium phosphate stones",
            "Uric acid stones",
            "Cystine stones",
            "Struvite (infection) stones — coordinated with urology",
            "Post-bariatric stone risk",
        ],
        "approach_intro": (
            "Stone prevention starts with knowing what kind of stone you make and what "
            "your urine chemistry actually shows:"
        ),
        "pillars": [
            ("Lab interpretation", "We review your 24-hour urine, stone composition, and metabolic workup with you."),
            ("Targeted diet", "Adjustments to fluid, sodium, animal protein, calcium, oxalate, and citrate based on your specific risk pattern."),
            ("Sustainable habits", "Realistic meal planning that fits your life and culture, not a generic restriction list."),
        ],
        "steps": [
            ("Records review", "Send us your stone analysis, 24-hour urine results, and recent labs before your first visit."),
            ("Initial consult", "60-minute visit to map out your specific drivers and a starting plan."),
            ("Follow-ups", "30-minute visits every 4–6 weeks, with repeat 24-hour urine at 3 months."),
            ("Long-term care", "Quarterly check-ins once you are stable."),
        ],
        "best_for": [
            "Patients who have formed two or more stones",
            "First-time formers with strong family history or metabolic risk",
            "Patients whose urology team has recommended dietary management",
        ],
        "not_for": [
            "Acute stone management (this is preventive care)",
            "Patients without a confirmed stone diagnosis",
            "Patients who decline 24-hour urine testing",
        ],
        "faq": [
            ("Do I need to cut out spinach forever?",
             "Almost certainly not. Oxalate restriction is one tool among many, and only some stone formers benefit. We tailor the recommendation to your urine chemistry."),
            ("Should I avoid calcium?",
             "No — that often makes stones worse. Adequate dietary calcium binds oxalate in the gut. The myth that calcium causes stones has been overturned for decades."),
            ("Will I need 24-hour urine testing?",
             "For recurrent stone formers, yes. It is the foundation of evidence-based prevention. We can help you arrange it through your local lab."),
            ("Do you replace my urologist?",
             "No. We complement urology and nephrology care by handling the nutrition piece in depth."),
        ],
    },
    {
        "slug": "diverticulitis-nutrition",
        "name": "Diverticulitis Nutrition",
        "short": "Diverticulitis Nutrition",
        "tagline": "Specialized dietetics for chronic and recurrent diverticulitis.",
        "accent": "#6b7d3a",
        "accent_soft": "#eef0e2",
        "category": "Medical Nutrition Therapy",
        "intro": (
            "Diverticulitis nutrition has changed significantly in the past decade. "
            "The old advice to avoid nuts, seeds, and popcorn has been disproven for "
            "most patients. Our dietitians provide evidence-based guidance for flares, "
            "recovery, and long-term prevention."
        ),
        "conditions": [
            "Acute uncomplicated diverticulitis recovery",
            "Chronic recurrent diverticulitis",
            "Post-surgical (resection) nutrition",
            "Smoldering diverticulitis",
            "SUDD (symptomatic uncomplicated diverticular disease)",
        ],
        "approach_intro": (
            "Eating after diverticulitis happens in stages — and getting each stage right "
            "matters more than blanket food avoidance:"
        ),
        "pillars": [
            ("Phased reintroduction", "Clear liquids → low-residue → high-fiber, paced to your symptoms and clinical course."),
            ("Long-term fiber strategy", "Building a 25–35g/day fiber pattern with the right balance of soluble and insoluble fiber."),
            ("Trigger identification", "Working through suspected triggers methodically rather than restricting everything at once."),
        ],
        "steps": [
            ("Initial intake", "Review your history, recent flares, and current eating pattern."),
            ("Phase plan", "Written meal plans for whatever stage you are in — flare, recovery, or maintenance."),
            ("Follow-ups", "Biweekly initially, then monthly as you stabilize."),
            ("Maintenance", "Quarterly check-ins for ongoing prevention."),
        ],
        "best_for": [
            "Patients who have had two or more episodes",
            "Patients recovering from a recent flare",
            "Anyone confused by conflicting diet advice",
        ],
        "not_for": [
            "Acute severe diverticulitis (this is outpatient nutrition, not emergency care)",
            "Patients with active abscess or perforation",
            "IBD masquerading as diverticulitis (we will refer)",
        ],
        "faq": [
            ("Can I eat nuts and seeds?",
             "Very likely yes. Large prospective studies have shown no increased risk of diverticulitis from nuts, seeds, or popcorn — and possibly a protective effect."),
            ("How much fiber should I eat?",
             "Long-term, most patients aim for 25–35g/day. The path to get there matters more than the destination — too fast and you will have symptoms."),
            ("What about low-FODMAP?",
             "Some patients with persistent symptoms between flares benefit from a structured low-FODMAP trial. We use it as a diagnostic tool, not a permanent diet."),
            ("Do probiotics help?",
             "Evidence is mixed. We discuss them case by case rather than recommending universally."),
        ],
    },
    {
        "slug": "tmj-therapy",
        "name": "TMJ Physical Therapy",
        "short": "TMJ Therapy",
        "tagline": "Specialized PT for temporomandibular joint dysfunction.",
        "accent": "#c2487a",
        "accent_soft": "#f7e4ec",
        "category": "Physical Therapy",
        "intro": (
            "TMJ disorders involve a complex interplay of jaw mechanics, neck posture, "
            "muscle tension, and stress. Our PTs are trained specifically in the "
            "craniomandibular system and coordinate with your dentist or oral surgeon "
            "as needed."
        ),
        "conditions": [
            "Jaw pain and clicking",
            "Temporal and tension-type headaches with TMJ origin",
            "Limited jaw opening (trismus)",
            "Disc displacement with and without reduction",
            "Bruxism-related muscle pain",
            "Post-surgical TMJ rehab",
        ],
        "approach_intro": (
            "Most TMJ pain responds to conservative care. Our virtual PT addresses the "
            "joint, the muscles, and the postural drivers — without rushing to splints or surgery:"
        ),
        "pillars": [
            ("Manual therapy guidance", "Self-mobilization techniques for the jaw and upper cervical spine, taught and supervised over video."),
            ("Targeted exercise", "Isometric strengthening, controlled mobility, and motor control retraining."),
            ("Postural and behavioral retraining", "Tongue position, resting jaw posture, daytime clenching awareness, and sleep ergonomics."),
        ],
        "steps": [
            ("Initial evaluation", "60-minute video assessment of jaw mechanics, cervical spine, and posture."),
            ("Active treatment", "Weekly 30-minute sessions with a daily home program."),
            ("Coordination", "We communicate with your dentist regarding splints when relevant."),
            ("Discharge", "Most patients see significant improvement in 6–10 weeks."),
        ],
        "best_for": [
            "Patients with TMJ symptoms over 4 weeks",
            "Those who have tried splints alone without full resolution",
            "Patients without local TMJ-specialized PT access",
        ],
        "not_for": [
            "Acute trauma or suspected fracture",
            "Severe joint locking requiring imaging or surgical evaluation",
            "Suspected systemic inflammatory arthritis (we refer)",
        ],
        "faq": [
            ("Can virtual PT really help my jaw?",
             "Yes — a substantial body of evidence supports exercise and manual self-mobilization for TMD, and PTs can teach these effectively over video."),
            ("Do I need a splint?",
             "Often not as a first step. We coordinate with your dentist if a splint is appropriate alongside therapy."),
            ("Why are my headaches involved?",
             "TMJ disorders frequently produce temporal, retro-orbital, and cervicogenic headaches. Treating the jaw and neck together typically reduces both."),
            ("Will Botox help?",
             "It can for severe bruxism-related muscle pain. We discuss when it is reasonable to ask your dentist or neurologist about it."),
        ],
    },
    {
        "slug": "dry-eye-treatment",
        "name": "Severe Dry Eye Treatment",
        "short": "Severe Dry Eye",
        "tagline": "Ophthalmology-led medication management for severe dry eye disease.",
        "accent": "#3b87bc",
        "accent_soft": "#e3eef6",
        "category": "Ophthalmology",
        "intro": (
            "For patients beyond the reach of artificial tears and warm compresses, "
            "severe dry eye requires structured medication management. Our ophthalmologists "
            "coordinate prescription therapy, autologous serum tears, and adjuncts — "
            "with in-person partners when in-office procedures are needed."
        ),
        "conditions": [
            "Severe evaporative dry eye and MGD",
            "Aqueous-deficient dry eye",
            "Sjögren's-related dry eye",
            "Post-LASIK chronic dry eye",
            "Graft-versus-host ocular disease",
            "Neurotrophic keratopathy (early stage)",
        ],
        "approach_intro": (
            "Severe dry eye is a chronic disease. We treat it like one — with structured "
            "longitudinal care rather than rotating through over-the-counter drops:"
        ),
        "pillars": [
            ("Prescription therapy", "Cyclosporine, lifitegrast, varenicline nasal spray, and topical corticosteroid courses managed over time."),
            ("Adjunct coordination", "Autologous serum tears, scleral lens referral, IPL/RF coordination, and punctal plug planning with local providers."),
            ("Lid and surface care", "Structured at-home protocols, lid hygiene, and demodex management when relevant."),
        ],
        "steps": [
            ("Initial visit", "Comprehensive dry eye history, symptom scores (OSDI, SPEED), and current regimen review."),
            ("Treatment plan", "Layered medication strategy with clear escalation criteria."),
            ("Monthly follow-ups", "Telehealth visits to titrate medications and track symptom scores."),
            ("In-person coordination", "We arrange office-based testing or procedures with a partner clinic when needed."),
        ],
        "best_for": [
            "Patients with severe symptoms despite over-the-counter regimens",
            "Patients on chronic prescription dry eye therapy seeking specialist oversight",
            "Patients in regions without dry-eye-specialist access",
        ],
        "not_for": [
            "Acute red eye, infection, or vision loss (urgent in-person care)",
            "Patients without a recent comprehensive eye exam",
            "Patients seeking primary in-person procedural care (we coordinate, not perform)",
        ],
        "faq": [
            ("Can dry eye really be managed over telehealth?",
             "Medication management, symptom tracking, and care coordination translate well to telehealth. We pair virtual visits with periodic in-person exams at a partner clinic."),
            ("How long until medications work?",
             "Cyclosporine and lifitegrast typically take 6–12 weeks. Varenicline nasal spray often works within days. We set expectations clearly upfront."),
            ("Do you handle scleral lenses?",
             "We coordinate with local scleral lens specialists. Severe dry eye often benefits from scleral lenses as part of a layered approach."),
            ("What about autologous serum tears?",
             "When indicated, we coordinate with compounding pharmacies and your local lab to arrange them."),
        ],
    },
    {
        "slug": "adhd-evaluations",
        "name": "Neuropsychological ADHD Evaluations",
        "short": "ADHD Evaluations",
        "tagline": "Comprehensive adult ADHD assessment via telehealth neuropsychology.",
        "accent": "#3f4ca3",
        "accent_soft": "#e6e8f3",
        "category": "Neuropsychology",
        "intro": (
            "A proper ADHD evaluation is more than a checklist. Our doctoral-level "
            "neuropsychologists perform full multi-method assessments — clinical "
            "interview, standardized testing, collateral reports, and rule-out of "
            "conditions that mimic ADHD — delivered over secure telehealth."
        ),
        "conditions": [
            "Adult ADHD (inattentive, hyperactive, or combined)",
            "ADHD with co-occurring anxiety, depression, or learning differences",
            "Suspected ADHD vs. autism, trauma, or sleep disorder",
            "Late-diagnosed ADHD in women",
            "Updated evaluations for college and graduate accommodations",
        ],
        "approach_intro": (
            "We use a structured, evidence-based protocol — not just symptom rating "
            "scales:"
        ),
        "pillars": [
            ("Clinical interview", "A 90–120 minute structured developmental and current-functioning interview."),
            ("Standardized testing", "Validated computerized attention tests and broader cognitive measures, administered via secure platform."),
            ("Collateral and corroboration", "Childhood records, parent or partner ratings, and validity measures to ensure accurate diagnosis."),
        ],
        "steps": [
            ("Records review", "We collect prior evaluations, school records, and rating scales before testing."),
            ("Testing days", "One or two sessions of 2–4 hours each over telehealth."),
            ("Feedback session", "A 60-minute session walking through results, diagnosis, and recommendations."),
            ("Written report", "A detailed report you can share with prescribers, employers, or schools."),
        ],
        "best_for": [
            "Adults wanting a thorough, defensible diagnosis",
            "Patients whose accommodations require neuropsychological documentation",
            "Patients with diagnostic ambiguity (ADHD vs. other conditions)",
        ],
        "not_for": [
            "Patients seeking a same-day diagnosis or prescription",
            "Patients unable to access a quiet, private space for testing",
            "Severe acute psychiatric crises (we refer first)",
        ],
        "faq": [
            ("How long does the full evaluation take?",
             "From intake to written report, typically 3–5 weeks. Active testing is 4–6 hours total."),
            ("Will the report be accepted for accommodations?",
             "Our reports follow the documentation standards of major employers, universities, and standardized test boards (LSAT, MCAT, USMLE, etc.)."),
            ("Is this covered by insurance?",
             "Some plans cover neuropsychological testing. We provide superbills and verify benefits before scheduling."),
            ("Do you prescribe ADHD medication?",
             "No — we are an evaluation service. We provide referrals to prescribers in your state."),
        ],
    },
    {
        "slug": "autism-evaluations",
        "name": "Autism Evaluations",
        "short": "Autism Evaluations",
        "tagline": "Telehealth autism diagnostic assessment for adults and children.",
        "accent": "#7e3fb0",
        "accent_soft": "#f0e8f6",
        "category": "Neurodevelopmental Assessment",
        "intro": (
            "Autism is often missed or misdiagnosed — particularly in adults, women, "
            "and people of color. Our clinicians use validated tools (ADOS-2 telehealth "
            "adaptations, ADI-R, and adult-specific measures) to deliver thorough, "
            "respectful diagnostic assessments."
        ),
        "conditions": [
            "Adult autism evaluations (including late-identified)",
            "Pediatric autism diagnostic assessments",
            "Differential diagnosis: autism vs. ADHD, social anxiety, OCD",
            "Autism with co-occurring conditions",
            "Updated evaluations for accommodations or services",
        ],
        "approach_intro": (
            "We approach autism assessment as a strengths-aware diagnostic process — "
            "not a deficit hunt:"
        ),
        "pillars": [
            ("Validated instruments", "Telehealth-adapted ADOS-2 modules, MIGDAS-2, ADI-R, RAADS-R, CAT-Q, and AQ-50 as appropriate."),
            ("Developmental history", "Detailed early-life information from caregivers when available."),
            ("Functional context", "Sensory, social, communication, and daily-life functioning across settings."),
        ],
        "steps": [
            ("Intake", "60-minute interview to clarify your goals and gather background."),
            ("Assessment sessions", "1–2 sessions of structured testing, typically 2–3 hours each."),
            ("Feedback", "60-minute session walking through findings together."),
            ("Written report", "A comprehensive, person-first written report with concrete recommendations."),
        ],
        "best_for": [
            "Adults seeking diagnostic clarity, including late-identified autism",
            "Families wanting a thorough pediatric evaluation",
            "Patients needing documentation for services, accommodations, or self-understanding",
        ],
        "not_for": [
            "Patients in acute crisis (we stabilize first or refer)",
            "Patients seeking only an informal screening (we do full assessments)",
            "Children too young for telehealth-adapted measures (we will recommend in-person)",
        ],
        "faq": [
            ("Can autism really be diagnosed over telehealth?",
             "For verbal adults and many children, yes — using telehealth-validated adaptations. We are explicit when a case warrants in-person referral."),
            ("Are you affirming?",
             "Yes. Our clinicians are trained in neurodiversity-affirming assessment. The goal is accurate understanding and useful recommendations, not pathologizing."),
            ("Will you give my child a 'level' diagnosis?",
             "DSM-5-TR levels (1, 2, 3) are part of the diagnostic framework when applicable. We use them carefully and explain what they mean for support."),
            ("How long is the full process?",
             "Typically 4–6 weeks from intake to written report."),
        ],
    },
    {
        "slug": "cannabis-use-disorder",
        "name": "Cannabis Use Disorder Treatment",
        "short": "Cannabis Use Disorder",
        "tagline": "Combined behavioral therapy and medical management for problematic cannabis use.",
        "accent": "#4a5d52",
        "accent_soft": "#ebeeec",
        "category": "Addiction Medicine & Behavioral Health",
        "intro": (
            "Roughly one in three people who use cannabis daily develop cannabis use "
            "disorder, and rates have risen substantially with the spread of high-potency "
            "concentrates and daily vape use. Our program combines evidence-based "
            "behavioral therapies with thoughtful medical support — treating CUD with "
            "the same seriousness as any other substance use disorder, without "
            "moralizing about cannabis itself."
        ),
        "conditions": [
            "Daily or near-daily cannabis use causing functional impact",
            "High-potency concentrate (dab, wax, distillate) dependence",
            "Cannabis vape and edible dependence",
            "Cannabis withdrawal syndrome",
            "Cannabinoid hyperemesis syndrome (CHS)",
            "CUD with co-occurring anxiety or depression",
            "CUD with co-occurring ADHD",
            "Medical cannabis patients seeking to reduce or stop",
            "Synthetic cannabinoid (HHC, THC-O, K2) cessation",
            "Relapse after prior quit attempts",
        ],
        "condition_details": [
            ("Cannabis use disorder",
             "DSM-5 cannabis use disorder is diagnosed when cannabis use causes meaningful problems across at least two of eleven domains — tolerance, withdrawal, unsuccessful quit attempts, time spent obtaining or using, role failures, and continued use despite consequences. Severity ranges from mild (2–3 criteria) to severe (6 or more). The clinical reality has shifted significantly in the past decade: today's daily user is often consuming cannabis many times more potent than a decade ago, frequently via concentrates that produce both faster tolerance and harder withdrawal. We treat the full severity spectrum."),
            ("Cannabis withdrawal syndrome",
             "Cannabis withdrawal is real, well-characterized, and a major reason people relapse during quit attempts. The classic profile includes irritability and anger, anxiety, sleep disturbance with vivid dreams, decreased appetite, restlessness, and depressed mood. Symptoms typically begin within 24–48 hours of last use, peak around days 2–6, and resolve over 1–3 weeks — though sleep can take longer to normalize. Knowing what to expect changes outcomes; we provide structured education and targeted support for the hardest first two weeks."),
            ("Cannabinoid hyperemesis syndrome",
             "CHS is increasingly common with chronic high-potency use: cyclical episodes of severe nausea, vomiting, and abdominal pain that paradoxically improve with hot showers and resolve only with sustained cannabis cessation. Many patients see multiple ER providers before a correct diagnosis is made. We coordinate with GI when needed and provide the structured cessation support that is the only definitive treatment."),
            ("High-potency concentrates and dabs",
             "Concentrate use behaves differently than flower use clinically. Tolerance escalates faster, withdrawal tends to be sharper, and the gap between casual and dependent use is shorter. We tailor our approach for concentrate-dominant users — including realistic expectations about the first two weeks, more intensive sleep and anxiety support, and concrete planning for social situations where dabs are normalized."),
            ("CUD with co-occurring anxiety, depression, or ADHD",
             "Many people use cannabis to manage anxiety, sleep, or attention symptoms — and cessation can transiently worsen what was being self-medicated. Our prescribers can address these underlying conditions directly with appropriate medications, while our therapists help build non-cannabis coping skills. Often the most important clinical work is identifying and treating the condition that was being medicated, so reduction or cessation is genuinely sustainable."),
            ("Medical cannabis patients reducing or stopping",
             "We work with patients who started cannabis under a medical recommendation but have come to feel it is no longer helping, or has begun causing more problems than it solves. The conversation here is different — it is about renegotiating your relationship with cannabis rather than treating an unequivocal disorder. We support stepwise reduction, full cessation, or pivots to alternative treatments depending on your goals."),
        ],
        "approach_intro": (
            "There is no FDA-approved medication specifically for CUD, but the evidence "
            "base for behavioral treatment is strong, and several off-label medications "
            "can meaningfully reduce withdrawal severity and craving. Our program combines:"
        ),
        "pillars": [
            ("CBT and motivational enhancement",
             "Weekly therapy combining cognitive-behavioral skills with motivational enhancement — the two approaches with the strongest CUD evidence base."),
            ("Medical support for withdrawal",
             "Off-label medication options (e.g., gabapentin, N-acetylcysteine, prazosin for sleep) carefully selected for your withdrawal profile, prescribed and monitored by an addiction medicine clinician."),
            ("Contingency management",
             "Structured incentive-based reinforcement for negative urine screens — the single most evidence-supported intervention for CUD when implementable."),
        ],
        "steps": [
            ("Intake", "Comprehensive medical and behavioral assessment, including use pattern, severity, and co-occurring conditions."),
            ("Quit-plan design (week 1)", "Choose taper or stop-date approach, set up withdrawal medications, and identify trigger situations."),
            ("Active phase (weeks 2–8)", "Weekly therapy and biweekly prescriber check-ins, with particular intensity through the withdrawal window."),
            ("Maintenance (weeks 9–16)", "Skill consolidation, relapse-prevention work, and gradual taper of any withdrawal medications."),
        ],
        "best_for": [
            "Adults using cannabis daily or near-daily with functional impact",
            "Concentrate or vape users wanting structured cessation support",
            "Medical cannabis patients reconsidering long-term use",
            "Patients who have tried to stop and run into severe withdrawal",
        ],
        "not_for": [
            "Patients in acute psychosis or severe psychiatric crisis (we stabilize first or refer)",
            "Patients seeking confirmation that their use is not problematic",
            "Adolescents under 18 (we refer to specialized adolescent programs)",
        ],
        "faq": [
            ("Is cannabis really addictive?",
             "Yes. About 9% of cannabis users overall — and roughly one in three daily users — meet criteria for cannabis use disorder. Risk is higher for people who started young and for high-potency products. Cannabis being legal in many places does not change its addictive potential."),
            ("Are there medications that help?",
             "No FDA-approved medication exists for CUD, but several off-label options have supportive evidence: gabapentin and N-acetylcysteine for craving and use reduction, prazosin for cannabis-related nightmares, and standard treatment of any underlying anxiety, depression, or ADHD that was being self-medicated."),
            ("How long does withdrawal last?",
             "Most acute withdrawal symptoms peak around days 2–6 and resolve within 1–3 weeks. Sleep disturbance and mood changes can take longer. Heavy concentrate users typically have a sharper, slightly longer withdrawal course."),
            ("Do I have to stop completely, or can I cut back?",
             "Both are valid goals. The evidence base is strongest for cessation, but harm-reduction approaches — reducing frequency, switching from concentrates back to lower-potency products, or eliminating high-risk patterns — are also legitimate paths. We work with your goals."),
            ("Will you tell my doctor or employer?",
             "No. Your care is confidential to the extent the law allows. We are a separate clinical service and only share information with your other providers if you ask us to."),
        ],
    },
    {
        "slug": "kyphosis-lordosis",
        "name": "Kyphosis & Lordosis Treatment",
        "short": "Kyphosis & Lordosis",
        "tagline": "Posture-focused physical therapy for excessive thoracic and lumbar spinal curvature.",
        "accent": "#5b6cad",
        "accent_soft": "#e9ecf6",
        "category": "Physical Therapy",
        "intro": (
            "Kyphosis and lordosis are postural and structural curvature conditions that "
            "respond well to targeted, progressive physical therapy when caught before "
            "they become rigid or symptomatic. Our program pairs you with a PT trained "
            "specifically in spinal posture rehabilitation — combining mobility work, "
            "deep postural muscle training, and day-to-day movement retraining over "
            "secure video."
        ),
        "conditions": [
            "Postural (flexible) thoracic kyphosis in adolescents and adults",
            "Scheuermann's kyphosis (non-surgical management)",
            "Hyperkyphosis of aging and osteoporosis-related curvature",
            "Post-surgical thoracic kyphosis rehabilitation",
            "Excessive lumbar lordosis (hyperlordosis) and anterior pelvic tilt",
            "Flat-back syndrome and lumbar hypolordosis",
            "Pregnancy- and postpartum-related lordotic posture",
            "Forward head posture and upper-crossed syndrome",
            "Lower-crossed syndrome with lumbar hyperlordosis",
            "Compensatory curvature from leg-length discrepancy",
        ],
        "condition_details": [
            ("Postural kyphosis",
             "Postural kyphosis is a flexible, correctable rounding of the upper back driven by muscle imbalance and habitual posture rather than vertebral wedging. It is by far the most common form we see — particularly in adolescents who spend long hours over screens, and in adults whose work involves sustained forward reach. Because the curvature is flexible, the prognosis with consistent therapy is excellent: most patients see meaningful change within 8–12 weeks. We focus on thoracic extension mobility, scapular and deep neck flexor strengthening, and rebuilding the postural endurance that allows the corrected position to feel effortless rather than held."),
            ("Scheuermann's kyphosis",
             "Scheuermann's is a structural kyphosis with anterior wedging of three or more consecutive vertebrae, typically presenting in adolescence. PT cannot reverse the wedging itself, but it remains the cornerstone of non-surgical care: maintaining mobility above and below the rigid segment, building the postural musculature that compensates for the curve, and reducing the secondary muscle pain that drives most symptoms. We coordinate with your spine specialist when bracing or surgical evaluation is appropriate."),
            ("Hyperkyphosis of aging",
             "After roughly age 50, kyphotic angle tends to increase — driven by a combination of disc degeneration, vertebral compression fractures, and postural muscle weakness. Hyperkyphosis is associated with falls, breathing difficulty, and reduced function. The good news: targeted exercise meaningfully reduces kyphotic angle and improves quality of life even in patients with osteoporosis. We use programs adapted from the published 'spinal proprioceptive extension exercise dynamic' (SPEED) and similar evidence-based protocols, modified for safety in osteoporotic patients."),
            ("Excessive lumbar lordosis",
             "Hyperlordosis — excessive inward curvature of the low back — typically goes hand-in-hand with anterior pelvic tilt, weak deep abdominals and glutes, and tight hip flexors and lumbar extensors. It often presents as low back pain with prolonged standing, difficulty engaging the core, and a visibly arched lower back. Treatment is rarely about 'flattening' the spine; it is about restoring the muscular balance that lets the pelvis sit neutrally. Our program targets hip flexor mobility, gluteal and deep abdominal activation, and posterior pelvic tilt control."),
            ("Flat-back and lumbar hypolordosis",
             "The opposite problem — too little lumbar curve — is increasingly common in patients with prolonged sitting, after certain spinal surgeries, or as part of a sagittal-plane imbalance. Flat-back posture reduces the spine's shock absorption and is strongly linked to fatigue, low back pain, and difficulty standing upright through the day. We work on segmental lumbar extension mobility, hip extension range, and the postural endurance needed to maintain a healthy lordotic curve."),
            ("Forward head and upper-crossed syndrome",
             "Forward head posture rarely exists in isolation; it travels with rounded shoulders, an elevated and protracted scapula, weak deep neck flexors, and tight upper trapezius and pectoralis muscles. This pattern — sometimes called upper-crossed syndrome — is a major driver of cervicogenic headaches, mid-thoracic pain, and shoulder impingement symptoms. Our program addresses the full chain rather than treating the neck in isolation."),
            ("Lower-crossed syndrome",
             "Lower-crossed syndrome pairs tight hip flexors and lumbar extensors with inhibited glutes and deep abdominals, producing the classic anterior pelvic tilt and lumbar hyperlordosis. It is one of the most common postural patterns we see and underlies a large share of mechanical low back pain. The treatment principles are well-established; what makes the difference is consistent, progressive programming and motor-control work that translates into how you actually stand, sit, and move."),
        ],
        "approach_intro": (
            "Postural curvature is rarely fixed by stretching alone. Lasting change "
            "requires mobility, strength, and motor control — applied consistently and "
            "progressed over time. Our PTs build programs around three pillars:"
        ),
        "pillars": [
            ("Targeted mobility",
             "Restoring the specific segmental mobility that postural curves require — thoracic extension for kyphosis, hip extension for lordosis — without overstretching segments that are already hypermobile."),
            ("Deep postural strengthening",
             "Rebuilding the deep neck flexors, scapular stabilizers, deep abdominals, and gluteal muscles that hold corrected posture without conscious effort."),
            ("Motor-control retraining",
             "Translating exercise gains into how you actually stand, sit, walk, and lift — the part most home programs miss, and the reason results stick."),
        ],
        "steps": [
            ("Initial evaluation", "60-minute video assessment including postural analysis, mobility testing, and functional movement screening."),
            ("Personalized program", "A written progressive program with video demonstrations, organized by phase (mobility → strength → integration)."),
            ("Weekly sessions", "30-minute follow-ups to progress your program, refine technique, and troubleshoot."),
            ("Discharge and maintenance", "Most patients see meaningful improvement in 8–12 weeks and graduate to an independent maintenance routine."),
        ],
        "best_for": [
            "Adolescents and adults with flexible postural kyphosis or lordosis",
            "Older adults with hyperkyphosis seeking evidence-based exercise",
            "Patients with chronic neck or back pain driven by postural patterns",
            "Patients without local access to posture-specialized PT",
            "Post-surgical patients past their early restrictions phase",
        ],
        "not_for": [
            "Acute spinal trauma or suspected vertebral fracture",
            "Adolescent idiopathic scoliosis as a primary diagnosis (we refer to Schroth-certified specialists)",
            "Severe rigid curves likely needing surgical evaluation",
            "Patients with red-flag neurological symptoms (progressive weakness, bowel or bladder changes)",
        ],
        "faq": [
            ("Can posture really be changed once you're an adult?",
             "Yes — flexible postural curves respond well to consistent therapy at any age. Even structural curves often improve in functional terms (pain, endurance, appearance) with the right program, even when the underlying skeletal anatomy doesn't change."),
            ("How long until I see results?",
             "Most patients notice changes in symptoms and ease of holding posture within 4–6 weeks. Visible postural change usually follows by 8–12 weeks. Long-standing patterns can take longer — six months is not unusual for full integration."),
            ("Do I need any equipment?",
             "Most programs use a yoga mat, a resistance band, and a foam roller. We sometimes recommend a small posture mirror or a phone tripod so you can self-check form. We tell you upfront before adding anything."),
            ("Will I need a brace?",
             "Most adults with flexible kyphosis or lordosis don't. Bracing is sometimes part of care for adolescent Scheuermann's kyphosis, and we coordinate with your spine specialist if it's appropriate. We do not prescribe braces ourselves."),
            ("What about scoliosis?",
             "Scoliosis (lateral curvature with rotation) is a different condition that benefits most from Schroth-certified care. We screen for it during evaluation and refer when it's the primary issue, while still helping with any kyphotic or lordotic component."),
            ("Is this covered by insurance?",
             "We are a cash-pay practice and provide superbills for out-of-network reimbursement. Many patients receive partial reimbursement under physical therapy benefits."),
        ],
    },
    {
        "slug": "migraine",
        "name": "Virtual Migraine Clinic",
        "short": "Migraine Clinic",
        "tagline": "Headache-neurology-led care for episodic and chronic migraine.",
        "accent": "#8b3a4e",
        "accent_soft": "#f3e3e7",
        "category": "Headache Neurology",
        "intro": (
            "Migraine is one of the most common and disabling neurological conditions, "
            "and most people who live with it never see a headache specialist. The wait "
            "for a headache neurologist commonly runs six months to a year, and primary "
            "care has limited time to work through the full preventive and acute "
            "pharmacologic ladder. Our program brings dedicated headache-neurology care "
            "to your home — including the modern preventive arsenal (CGRP antibodies, "
            "gepants), acute therapy optimization, behavioral therapy integration, and "
            "structured medication-overuse withdrawal when needed."
        ),
        "conditions": [
            "Episodic migraine, with and without aura",
            "Chronic migraine (≥15 headache days per month)",
            "Vestibular migraine and migrainous vertigo",
            "Menstrual and hormonally-driven migraine",
            "Hemiplegic migraine",
            "Migraine with brainstem aura (basilar-type)",
            "Status migrainosus (refractory acute attack management)",
            "Medication overuse headache (MOH)",
            "New daily persistent headache (NDPH)",
            "Cluster headache and other trigeminal autonomic cephalalgias",
            "Post-concussive headache with migrainous features",
            "Migraine in pregnancy and lactation (coordinated with OB)",
            "Adolescent migraine (age 12 and up)",
            "Refractory migraine after multiple preventive failures",
        ],
        "condition_details": [
            ("Episodic and chronic migraine",
             "The single most consequential question in migraine care is whether you are episodic (fewer than 15 headache days per month) or chronic (15 or more, with at least 8 meeting full migraine criteria). The treatment ladders are different, the preventive evidence base is different, and the insurance coverage criteria are different. Many patients sit just on either side of the line and slide between categories — often without anyone formally tracking it. We start every program with a structured headache calendar so we know which patient we are actually treating, and we re-stage at every visit."),
            ("Vestibular migraine",
             "Vestibular migraine is one of the most common causes of recurrent vertigo in adults and one of the most under-diagnosed. Many patients spend years cycling through ENT, cardiology, and neurology workups before someone connects episodic vertigo, motion sensitivity, and a personal or family history of migraine. The treatment principles overlap with classic migraine — preventive medication, trigger work, vestibular rehab — but the acute toolkit is narrower and the response timelines are different. We treat vestibular migraine with the same neurologists who treat the rest of our migraine population, in coordination with vestibular PT when indicated."),
            ("Menstrual and hormonal migraine",
             "Menstrual migraine — attacks tightly clustered around the perimenstrual window — affects a large share of women with migraine and often responds poorly to the same preventive that works the rest of the month. Targeted strategies include scheduled mini-prevention with long-acting triptans or NSAIDs across the perimenstrual window, hormonal stabilization in coordination with gynecology, and CGRP antagonists timed to the cycle. Perimenopause adds a layer: migraine frequency commonly worsens for several years before stabilizing post-menopause, and managing that transition deliberately can change the trajectory."),
            ("Medication overuse headache",
             "Medication overuse headache is a paradox at the heart of migraine care: the acute medications that abort individual attacks can, when used too frequently, perpetuate the underlying headache disorder. The thresholds are well-established (roughly 10 days per month for triptans, opioids, ergots, or combination analgesics; 15 for simple analgesics). Recognizing and treating MOH is one of the most clinically rewarding things we do — many patients see their baseline headache pattern improve dramatically once the overused medication is withdrawn and a proper preventive is in place. The first two weeks of withdrawal are the hard part, and we plan for them deliberately with bridge therapies and structured check-ins."),
            ("Cluster headache",
             "Cluster headache is a distinct trigeminal autonomic cephalalgia with a different clinical profile, treatment toolkit, and natural history than migraine. Attacks are short (15–180 minutes), severe, strictly unilateral, and accompanied by autonomic features (tearing, conjunctival injection, ptosis, rhinorrhea). Effective acute therapy is high-flow oxygen and subcutaneous sumatriptan; preventive options include verapamil at neurology-specific dosing, galcanezumab, and short corticosteroid bridges during a cluster period. We treat cluster headache with the same neurologist team and coordinate oxygen prescriptions through your local DME provider."),
            ("Refractory migraine after multiple preventive failures",
             "A meaningful share of patients reach us after trying — and not tolerating or not responding to — three, four, or more preventive medications. Modern headache neurology has a structured way to think about this: confirming the diagnosis is correct (vestibular migraine, NDPH, and chronic tension-type can masquerade as refractory migraine), identifying any unaddressed contributors (sleep apnea, MOH, hormonal drivers, untreated mood symptoms), and then sequencing the newer mechanism classes (CGRP monoclonal antibodies, atogepant, Botox for chronic migraine) thoughtfully rather than adding them on top of a regimen that is already failing."),
        ],
        "approach_intro": (
            "Migraine care has been transformed in the past decade by CGRP-targeted "
            "therapies. The challenge is no longer a lack of options — it is matching "
            "the right combination of acute, preventive, and behavioral care to each "
            "patient, and adjusting it deliberately over time. Our headache neurologists "
            "build programs around three pillars:"
        ),
        "pillars": [
            ("Acute therapy optimization",
             "Right-sized acute regimens using triptans, gepants (rimegepant, ubrogepant, zavegepant), ditans, anti-emetics, and rescue planning — with explicit attention to the use-frequency thresholds that protect against medication overuse headache."),
            ("Preventive strategy",
             "Modern preventive sequencing: CGRP monoclonal antibodies (erenumab, fremanezumab, galcanezumab, eptinezumab), atogepant, traditional preventives (topiramate, beta-blockers, tricyclics, candesartan), and Botox-for-chronic-migraine coordination when indicated."),
            ("Lifestyle and behavioral integration",
             "The SEEDS framework (sleep, exercise, eat, diary, stress) implemented as concrete habits, with referral to migraine-specific CBT, biofeedback, and neuromodulation devices (Cefaly, Nerivio, gammaCore) when they fit your pattern."),
        ],
        "steps": [
            ("Comprehensive intake", "60-minute visit covering full headache history, prior treatment ladder, family history, and red-flag screening. We set up a structured digital headache calendar before you leave."),
            ("Personalized treatment plan", "A written plan layering acute therapy, a preventive strategy, and behavioral integration — with explicit response criteria and timelines so you know what 'working' looks like."),
            ("Active titration", "Monthly visits over 3–4 months while preventives reach steady state and acute regimens are refined. Most CGRP antibodies need 8–12 weeks for a fair trial; oral preventives need careful dose titration."),
            ("Maintenance", "Quarterly visits once stable, with messaging access for breakthrough flares and a planned re-evaluation of preventive duration after 6–12 months of good control."),
        ],
        "best_for": [
            "Adults with 4 or more migraine days per month",
            "Patients with chronic migraine (≥15 headache days per month)",
            "Patients who have failed two or more preventive medications",
            "Patients without local headache-neurologist access",
            "Patients with suspected medication overuse headache seeking structured withdrawal",
            "Patients exploring CGRP-targeted therapies and needing prior-auth support",
        ],
        "not_for": [
            "Thunderclap headache, worst-headache-of-life, or sudden focal neurological deficits — call 911 or go to the nearest ED",
            "New headache patterns with red-flag features that need in-person workup before management",
            "Children under 12 (we refer to pediatric headache specialists)",
            "Patients seeking opioid or barbiturate-containing prescriptions for migraine — we do not prescribe these for headache",
            "Acute pregnancy without an OB already co-managing care",
        ],
        "faq": [
            ("Can migraine really be diagnosed and managed over telehealth?",
             "Yes. Migraine diagnosis is fundamentally clinical — based on history against ICHD-3 criteria, not imaging or labs. Telehealth is well-suited to it. When a presentation has red flags or warrants imaging, a focused exam, or in-office procedures, we coordinate with a local clinic rather than skipping the workup."),
            ("What about CGRP medications?",
             "CGRP monoclonal antibodies and the gepants are now first-line preventive options for many patients, and we routinely prescribe them. We also help with prior authorizations and patient assistance programs, since coverage varies wildly by plan and the paperwork burden is real."),
            ("Do you do Botox for chronic migraine?",
             "We design and direct the regimen, but the injections themselves are an in-person procedure. We coordinate the PREEMPT protocol with a partner injector or your local neurologist."),
            ("Will I be on preventives forever?",
             "Often no. Many patients taper off preventives after 6–12 months of stable control. We plan the taper carefully because rebound is real and the goal is durable improvement, not a permanent prescription."),
            ("What if I have medication overuse headache?",
             "Withdrawal from overused acute medications is one of the most clinically rewarding things we do — and one of the hardest first two weeks. We provide a structured plan that includes a bridge therapy (often a short steroid course or DHE alternative), a clear acute-medication ceiling going forward, and frequent check-ins through the rough window."),
            ("Can you handle cluster headache?",
             "Yes. Cluster headache responds to a different toolkit (high-flow oxygen, subcutaneous sumatriptan, verapamil at headache-specific dosing, galcanezumab, short steroid bridges) and we manage it with the same neurologist team. We coordinate oxygen prescriptions through your local DME provider."),
            ("What about devices like Cefaly or Nerivio?",
             "Neuromodulation devices have a real role for the right patient — particularly those who want to minimize medications, are pregnant, or are layering acute support around a stable preventive. We discuss them case by case and help with prescriptions where required."),
            ("Is this covered by insurance?",
             "We are a cash-pay practice and provide superbills for out-of-network reimbursement. Prescribed medications run through your normal pharmacy benefit, and we handle prior authorizations as part of the visit."),
        ],
    },
]


def render_clinic_page(clinic):
    accent = clinic["accent"]
    soft = clinic["accent_soft"]
    name = html.escape(clinic["name"])
    tagline = html.escape(clinic["tagline"])
    intro = html.escape(clinic["intro"])
    category = html.escape(clinic["category"])
    approach_intro = html.escape(clinic["approach_intro"])

    conditions_html = "\n".join(
        f"      <li>{html.escape(c)}</li>" for c in clinic["conditions"]
    )
    pillars_html = "\n".join(
        f'      <div class="pillar"><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div>'
        for t, d in clinic["pillars"]
    )
    steps_html = "\n".join(
        f'      <li><div class="step-num">{i+1}</div><div class="step-body"><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div></li>'
        for i, (t, d) in enumerate(clinic["steps"])
    )
    best_html = "\n".join(
        f"        <li>{html.escape(b)}</li>" for b in clinic["best_for"]
    )
    not_html = "\n".join(
        f"        <li>{html.escape(b)}</li>" for b in clinic["not_for"]
    )
    faq_html = "\n".join(
        f'      <details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>'
        for q, a in clinic["faq"]
    )

    if clinic.get("condition_details"):
        detail_html = "\n".join(
            f'        <article class="condition-detail"><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></article>'
            for t, d in clinic["condition_details"]
        )
        condition_details_section = f"""
    <section class="section alt">
      <div class="container narrow">
        <h2>Conditions in depth</h2>
        <div class="condition-details">
{detail_html}
        </div>
      </div>
    </section>"""
    else:
        condition_details_section = ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} — {SITE_NAME}</title>
  <meta name="description" content="{tagline}">
  <link rel="stylesheet" href="../assets/style.css">
  <style>
    :root {{
      --accent: {accent};
      --accent-soft: {soft};
    }}
  </style>
</head>
<body>
  <nav class="topnav">
    <a class="brand" href="../">{SITE_NAME}</a>
    <a class="nav-link" href="../">All clinics</a>
  </nav>

  <header class="hero">
    <div class="hero-inner">
      <span class="eyebrow">{category}</span>
      <h1>{name}</h1>
      <p class="tagline">{tagline}</p>
      <a class="cta" href="#contact">Request a consultation</a>
    </div>
  </header>

  <main>
    <section class="overview section">
      <div class="container narrow">
        <p class="lede">{intro}</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>Conditions we treat</h2>
        <ul class="check-list">
{conditions_html}
        </ul>
      </div>
    </section>
{condition_details_section}
    <section class="section">
      <div class="container">
        <h2>Our approach</h2>
        <p class="lede">{approach_intro}</p>
        <div class="pillars">
{pillars_html}
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>How it works</h2>
        <ol class="steps">
{steps_html}
        </ol>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Is this right for you?</h2>
        <div class="two-col">
          <div class="col">
            <h3>Best for</h3>
            <ul>
{best_html}
            </ul>
          </div>
          <div class="col">
            <h3>Not the right fit</h3>
            <ul>
{not_html}
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container narrow">
        <h2>Frequently asked questions</h2>
        <div class="faq">
{faq_html}
        </div>
      </div>
    </section>

    <section id="contact" class="section cta-section">
      <div class="container narrow">
        <h2>Ready to start?</h2>
        <p>Schedule a free 15-minute discovery call to see if this program fits your needs.</p>
        <button class="cta" onclick="alert('This is a concept site. No real bookings.')">Request consultation</button>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p class="disclaimer">
        <strong>Concept site.</strong> This page describes a hypothetical virtual clinic
        and is for design and discussion purposes only. Nothing here is medical advice.
        No bookings are real. No personal health information is collected.
      </p>
      <p><a href="../">← Back to all clinics</a></p>
    </div>
  </footer>
</body>
</html>
"""


def render_index():
    cards = []
    for c in CLINICS:
        cards.append(f'''      <a class="card" href="{c["slug"]}/" style="--accent: {c["accent"]}; --accent-soft: {c["accent_soft"]};">
        <span class="card-eyebrow">{html.escape(c["category"])}</span>
        <h3>{html.escape(c["name"])}</h3>
        <p>{html.escape(c["tagline"])}</p>
        <span class="card-link">Learn more →</span>
      </a>''')
    cards_html = "\n".join(cards)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{SITE_NAME} — Specialty virtual care concepts</title>
  <meta name="description" content="{SITE_TAGLINE}">
  <link rel="stylesheet" href="assets/style.css">
  <style>
    :root {{
      --accent: #2c3e50;
      --accent-soft: #ecf0f1;
    }}
  </style>
</head>
<body>
  <nav class="topnav">
    <a class="brand" href="./">{SITE_NAME}</a>
  </nav>

  <header class="hero hero-index">
    <div class="hero-inner">
      <span class="eyebrow">Concept portfolio</span>
      <h1>Specialty virtual care, designed deliberately</h1>
      <p class="tagline">{SITE_TAGLINE} Each program is built around a single condition or population — chosen because the standard of care is fragmented, hard to access, or under-served by general telehealth.</p>
    </div>
  </header>

  <main>
    <section class="section">
      <div class="container">
        <h2>The clinics</h2>
        <div class="grid">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container narrow">
        <h2>Why specialty-specific?</h2>
        <p class="lede">
          Generalist telehealth works for routine primary care. It struggles with conditions
          that need clinicians with specific post-graduate training, longitudinal protocols,
          and care coordination across providers. Each program here is designed around the
          actual evidence base and patient journey for a single condition — not bolted on
          to an existing platform.
        </p>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p class="disclaimer">
        <strong>Concept portfolio.</strong> These pages describe hypothetical virtual clinics
        for design and discussion purposes only. Nothing here is medical advice. No bookings
        are real. No personal health information is collected.
      </p>
    </div>
  </footer>
</body>
</html>
"""


def main():
    # Write index
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")

    # Write each clinic
    for clinic in CLINICS:
        clinic_dir = ROOT / clinic["slug"]
        clinic_dir.mkdir(exist_ok=True)
        (clinic_dir / "index.html").write_text(render_clinic_page(clinic), encoding="utf-8")

    # Touch .nojekyll
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built index + {len(CLINICS)} clinic pages.")


if __name__ == "__main__":
    main()
