from rules import career_profiles

def recommend_careers(user_skills):

    recommendations = []

    reasoning_steps = []

    for career, details in career_profiles.items():

        required_skills = details["skills"]

        matched = len(
            set(user_skills) &
            set(required_skills)
        )

        score = round(
            (matched / len(required_skills)) * 100
        )

        if score > 0:

            reasoning_steps.append(
                f"{career}: matched {matched} out of {len(required_skills)} skills"
            )

            recommendations.append({
                "career": career,
                "score": score,
                "salary": details["salary"],
                "description": details["description"]
            })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations, reasoning_steps