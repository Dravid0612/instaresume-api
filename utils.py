import re

def generate_summary(text):
    if not text:
        return 'No text provided.'
    # simple extractive summary: first 2–3 sentences
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    return ' '.join(sentences[:3])

def generate_headline(text):
    if not text:
        return 'Professional | Problem Solver'
    # pick some frequent capitalized words or common skill tokens
    tokens = re.findall(r'\b[A-Za-z0-9+#.+-]{2,}\b', text)
    # common skill set fallback
    fallback = ['Python', 'SQL', 'Communication', 'Leadership']
    freq = {}
    for t in tokens:
        t_low = t.lower()
        freq[t_low] = freq.get(t_low, 0) + 1
    sorted_tokens = sorted(freq.items(), key=lambda x: -x[1])
    picks = [t[0].capitalize() for t in sorted_tokens[:4]]
    picks = [p for p in picks if not p.isdigit()]
    if not picks:
        picks = fallback
    return ' | '.join(picks[:4])

def extract_skills(text):
    if not text:
        return []
    common_skills = [
        "Python", "Java", "C++", "SQL", "Machine Learning", "HTML",
        "CSS", "JavaScript", "Leadership", "Communication", "Data Analysis",
        "TensorFlow", "PyTorch", "React", "Node.js"
    ]
    found = [s for s in common_skills if s.lower() in text.lower()]
    # keep original order and unique
    seen = set()
    out = []
    for s in found:
        if s not in seen:
            out.append(s)
            seen.add(s)
    return out

def generate_linkedin_about(text):
    if not text:
        return (
            "Motivated professional with a passion for learning and problem solving. "
            "Skilled at turning ideas into deliverables and focused on measurable impact."
        )
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    first = sentences[0] if sentences else ''
    about = (
        f"{first} I am a results-driven professional with experience in relevant domains. "
        "I focus on clarity, measurable impact and continuous learning."            )
    return about
