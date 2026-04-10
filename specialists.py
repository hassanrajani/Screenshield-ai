import requests

# ─────────────────────────────────────────────
# HARDCODED SPECIALIST DATA BY CITY
# ─────────────────────────────────────────────

SPECIALISTS = {
    "Karachi": [
        {
            "name": "Umang Mental Health Helpline",
            "type": "Helpline",
            "phone": "0317-4288665",
            "description": "Free mental health helpline offering counseling and emotional support."
        },
        {
            "name": "Karachi Psychiatric Hospital",
            "type": "Hospital",
            "phone": "021-99261001",
            "description": "Government psychiatric facility providing inpatient and outpatient mental health services."
        },
        {
            "name": "The Counseling Clinic (Karachi)",
            "type": "Clinic",
            "phone": "021-35830528",
            "description": "Private clinic offering therapy for anxiety, depression, and stress management."
        },
        {
            "name": "Rozan Counseling Helpline",
            "type": "Helpline",
            "phone": "051-2890505",
            "description": "Psychosocial support helpline for individuals facing emotional distress."
        },
    ],
    "Lahore": [
        {
            "name": "Fountain House Lahore",
            "type": "Clinic",
            "phone": "042-35761999",
            "description": "Rehabilitation and support center for individuals with mental illness."
        },
        {
            "name": "Punjab Institute of Mental Health",
            "type": "Hospital",
            "phone": "042-99231701",
            "description": "Leading government psychiatric hospital in Punjab offering full mental health services."
        },
        {
            "name": "Umang Helpline",
            "type": "Helpline",
            "phone": "0317-4288665",
            "description": "Free mental health helpline available across Pakistan."
        },
        {
            "name": "Mind & Brain Clinic Lahore",
            "type": "Clinic",
            "phone": "042-35761000",
            "description": "Private psychiatric and psychological services for all age groups."
        },
    ],
    "Islamabad": [
        {
            "name": "Rozan Counseling Helpline",
            "type": "Helpline",
            "phone": "051-2890505",
            "description": "Psychosocial support and counseling for emotional and mental health issues."
        },
        {
            "name": "Institute of Psychiatry (Rawalpindi)",
            "type": "Hospital",
            "phone": "051-9281386",
            "description": "Government psychiatric institute serving Islamabad and Rawalpindi region."
        },
        {
            "name": "Willing Ways Islamabad",
            "type": "Clinic",
            "phone": "051-2611407",
            "description": "Rehabilitation and mental wellness center for addiction and psychological disorders."
        },
        {
            "name": "Umang Mental Health Helpline",
            "type": "Helpline",
            "phone": "0317-4288665",
            "description": "Free nationwide mental health support helpline."
        },
    ],
    "Rawalpindi": [
        {
            "name": "Institute of Psychiatry (Rawalpindi)",
            "type": "Hospital",
            "phone": "051-9281386",
            "description": "Government psychiatric institute serving Rawalpindi and Islamabad."
        },
        {
            "name": "Rozan Counseling Helpline",
            "type": "Helpline",
            "phone": "051-2890505",
            "description": "Psychosocial support helpline for individuals in distress."
        },
        {
            "name": "Umang Mental Health Helpline",
            "type": "Helpline",
            "phone": "0317-4288665",
            "description": "Free mental health helpline available across Pakistan."
        },
        {
            "name": "Al-Shifa Trust Mental Health",
            "type": "Clinic",
            "phone": "051-5487800",
            "description": "Affordable mental health consultations and therapy services."
        },
    ],
    "Peshawar": [
        {
            "name": "Lady Reading Hospital Psychiatry",
            "type": "Hospital",
            "phone": "091-9211330",
            "description": "Psychiatric ward at the largest public hospital in KPK."
        },
        {
            "name": "Umang Mental Health Helpline",
            "type": "Helpline",
            "phone": "0317-4288665",
            "description": "Free mental health helpline available across Pakistan."
        },
        {
            "name": "Khyber Teaching Hospital Psychiatry",
            "type": "Hospital",
            "phone": "091-9216480",
            "description": "Government teaching hospital with dedicated psychiatric services."
        },
        {
            "name": "Rozan Counseling Helpline",
            "type": "Helpline",
            "phone": "051-2890505",
            "description": "Nationwide psychosocial support and counseling helpline."
        },
    ],
    "Quetta": [
        {
            "name": "Bolan Medical Complex Psychiatry",
            "type": "Hospital",
            "phone": "081-9201080",
            "description": "Main government hospital in Balochistan with psychiatric services."
        },
        {
            "name": "Umang Mental Health Helpline",
            "type": "Helpline",
            "phone": "0317-4288665",
            "description": "Free mental health helpline available across Pakistan."
        },
        {
            "name": "Civil Hospital Quetta Psychiatry",
            "type": "Hospital",
            "phone": "081-9202031",
            "description": "Government hospital offering mental health consultations."
        },
        {
            "name": "Rozan Counseling Helpline",
            "type": "Helpline",
            "phone": "051-2890505",
            "description": "Psychosocial support helpline serving all of Pakistan."
        },
    ],
    "Multan": [
        {
            "name": "Nishtar Hospital Psychiatry",
            "type": "Hospital",
            "phone": "061-9200300",
            "description": "Major government hospital in South Punjab with psychiatric ward."
        },
        {
            "name": "Umang Mental Health Helpline",
            "type": "Helpline",
            "phone": "0317-4288665",
            "description": "Free mental health helpline available across Pakistan."
        },
        {
            "name": "Fountain House Multan",
            "type": "Clinic",
            "phone": "061-4510000",
            "description": "Mental health rehabilitation and support center."
        },
        {
            "name": "Rozan Counseling Helpline",
            "type": "Helpline",
            "phone": "051-2890505",
            "description": "Nationwide psychosocial support helpline."
        },
    ],
    "Faisalabad": [
        {
            "name": "Allied Hospital Psychiatry",
            "type": "Hospital",
            "phone": "041-9220071",
            "description": "Government hospital in Faisalabad with dedicated psychiatric services."
        },
        {
            "name": "Umang Mental Health Helpline",
            "type": "Helpline",
            "phone": "0317-4288665",
            "description": "Free mental health helpline available across Pakistan."
        },
        {
            "name": "DHQ Hospital Faisalabad Psychiatry",
            "type": "Hospital",
            "phone": "041-9220033",
            "description": "District headquarters hospital offering mental health consultations."
        },
        {
            "name": "Rozan Counseling Helpline",
            "type": "Helpline",
            "phone": "051-2890505",
            "description": "Psychosocial support helpline serving all of Pakistan."
        },
    ],
}

# Fallback — shown when city is not in our list
NATIONAL_HELPLINES = [
    {
        "name": "Umang Mental Health Helpline",
        "type": "Helpline",
        "phone": "0317-4288665",
        "description": "Free mental health helpline offering counseling and emotional support nationwide."
    },
    {
        "name": "Rozan Counseling Helpline",
        "type": "Helpline",
        "phone": "051-2890505",
        "description": "Psychosocial support helpline for individuals facing emotional distress."
    },
    {
        "name": "Rescue Emergency",
        "type": "Emergency",
        "phone": "1122",
        "description": "Emergency rescue service available across Pakistan."
    },
    {
        "name": "Edhi Foundation",
        "type": "Helpline",
        "phone": "115",
        "description": "Social welfare helpline providing support and referrals across Pakistan."
    },
]


# ─────────────────────────────────────────────
# INTERNET CHECK
# ─────────────────────────────────────────────

def is_online():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except Exception:
        return False


# ─────────────────────────────────────────────
# GET SPECIALISTS FOR A CITY
# ─────────────────────────────────────────────

def get_specialists(city_key):
    return SPECIALISTS.get(city_key, NATIONAL_HELPLINES)
