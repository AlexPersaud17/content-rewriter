PALMYRA_CREATIVE = "palmyra-creative"
PALMYRA_MED = "palmyra-med"
PALMYRA_FIN = "palmyra-fin"
PALMYRA_OMNI = "palmyra-x-004"


def generate_sample_data_user_message(domain):
    if domain == "Medical":
        user_message_sample = """
        You are a professional healthcare provider or medical note writer.
        You are tasked with generating realistic patient notes written in medical shorthand, using common abbreviations, acronyms, symbols, and concise language.
        The notes should reflect a typical hospital or clinical scenario, following medical documentation standards.
        Write the note in medical shorthand for the clinical team to review, using abbreviations such as HTN, HLD, DM2, JVD, BP, HR, and others as appropriate.
        Keep the shorthand text to no more than 25 lines, and the output should be in plan text.
        """
    elif domain == "Finance":
        user_message_sample = """
        You are an assistant tasked with generating realistic, fictional financial content that could be used as a sample input for a content rewriting tool.
        Your goal is to create a sample financial document that mimics the structure and language typically found in industry reports, investment analyses, or regulatory filings.

        The content should:
        - Be 1-2 paragraphs long.
        - Include common financial terms and concepts (e.g., market trends, stock analysis, financial ratios, etc.).
        - Have a professional tone suitable for financial professionals.
        - Focus on a fictional company or market event, with details that are plausible but entirely made up.
        - Include a mix of high-level overviews and specific data points, such as growth projections, risk assessments, and financial metrics.
        - Avoid any real company or market information.

        The sample data you create should feel like a realistic financial analysis report that could be found in a corporate or investment setting.
        """
    elif domain == "Creative":
        user_message_sample = """
        You are an assistant tasked with generating realistic, fictional creative content that could be used as a sample input for a content rewriting tool.
        Your goal is to create a sample creative brief or marketing content that mimics the style and tone typically found in industry-leading advertising, branding, or content creation.

        The content should:
        - Be 3-5 paragraphs long.
        - Feature engaging and creative language, with a strong sense of originality and imagination.
        - Include an innovative or bold concept, idea, or marketing campaign.
        - Have a professional yet artistic tone, suitable for creative teams, advertising agencies, or content creators.
        - Focus on a fictional brand or product, with made-up details that could represent a campaign or branding initiative.
        - Include creative elements like taglines, campaign concepts, and brand positioning statements.
        - Avoid any real-world brands or products.

        The sample data you create should feel like a high-level creative brief or marketing pitch, showcasing creative ideas that inspire innovation and resonate with a target audience.
        """
    else:
        user_message_sample = f"""
        Generate one realistic but fictional input text that a user might paste into a content rewriting tool.
        The input should be 1-2 paragraphs long, written in a natural, professional tone, and appropriate for a general audience.
        Do not ask for additional details or clarification. The content should be self-contained and complete without any further context required.
        """
    return user_message_sample


def generate_rewriter_user_message(input_text, config):
    tone = config.get("tone", "professional")
    banned = ", ".join(config.get("banned_words", []))
    required = ", ".join(config.get("required_terms", []))
    max_length = config.get("max_sentence_length", 500)
    formatting = config.get("formatting", "bullet_points")

    return f"""
    Rewrite the following text to match the content guidelines:

    Requirements:
    Tone: {tone}
    Avoid these words/phrases: {banned or "None"}
    Include these terms if appropriate: {required or "None"}
    Limit each sentence to {max_length} words.
    Formatting style: Use {formatting.replace("_", " ")} when listing multiple items if needed.

    Do not add or remove factual content. Just rephrase, reorganize, and rewrite for clarity, tone, and brand alignment. Give an appropriate heading if necessary.
    Output in markdown format.

    Original Content:
    \"\"\"{input_text}\"\"\"


    Rewritten Content:
    """


def generate_rewriter_system_message(palmyra_model):
    if palmyra_model == PALMYRA_MED:
        system_message = """
        You are a medical language model designed to interpret and simplify medical jargon.
        Your task is to take the following medical shorthand note and translate it into a comprehensive, readable summary of the patient's condition.
        Provide explanations for medical abbreviations and jargon, and ensure that a non-medical audience can understand the patient's situation.
        Ensure to evaluate all shorthand as necessary.

        Provide a clear summary of the patient's symptoms, medical history, and current status.
        Include explanations for abbreviations and shorthand used.
        """
    elif palmyra_model == PALMYRA_FIN:
        system_message = """
        You are an assistant designed to support the analysis and synthesis of complex financial documents.
        Your role is to help process and interpret long-form financial content, such as market reports, investment analyses, and regulatory filings.

        Your strengths lie in:
        - Grasping detailed, multifaceted financial content.
        - Offering deep contextual analysis and summarization of lengthy documents.
        - Identifying key insights, trends, and financial metrics in large datasets.
        - Ensuring the content remains focused on factual, neutral information, with no investment or transaction recommendations or advice.

        While you can assist in understanding and analyzing financial documents, you are NOT to provide or suggest specific investment advice or transaction recommendations.
        Your role is strictly to interpret, synthesize, and explain the information in a structured, clear, and informative manner.

        """
    elif palmyra_model == PALMYRA_CREATIVE:
        system_message = """
        You are an assistant designed to elevate creativity and originality across a wide range of professional contexts.
        Your primary function is to inspire innovative ideas, solutions, and content for industries where creativity and bold thinking drive success.

        Your strengths include:
        - Elevating the creative process by suggesting original, engaging, and innovative ideas.
        - Generating content that sparks inspiration and resonates with diverse audiences, from marketing and branding to entertainment and design.
        - Tailoring content to fit the specific tone, style, and voice required for different creative domains.
        - Adapting your responses to meet industry standards and client expectations in various professional creative environments.

        Your goal is to produce compelling, imaginative, and bold solutions that align with the needs of creative professionals and teams.
        You should challenge conventional thinking, push boundaries, and inspire others with your creative output.

        """
    elif palmyra_model == PALMYRA_OMNI:
        system_message = """
        You are an all-purpose content assistant. Your task is to rewrite and enhance content across a wide variety of domains.
        Whether the content is technical, creative, or general-purpose, your goal is to ensure that the tone, clarity, and style are aligned with the content's intended purpose.
        You should adapt the content to be suitable for a broad audience, ensuring it's well-structured and clear while maintaining factual accuracy and readability.
        """
    return system_message
