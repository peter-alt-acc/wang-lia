from config import gemini_client, system_prompt
from config import ResponseSchema

def command_ch(input):

    try:
        response = gemini_client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=input,
            config={
                "response_mime_type": "application/json",
                "response_schema": ResponseSchema,
                "system_instruction": system_prompt,
            },
        )

        try:
            result = ResponseSchema.model_validate_json(response.text)
        except Exception as e:
            print("Gemini response parsing failed:", e)
            return

    except Exception as e:
        print("Gemini failed:", e)
        return

    tg_result = (
        f"<b>Input: </b>\n<blockquote>{input}</blockquote>\n"
        f"<b>Input Translation: </b>\n<blockquote>{result.InputCH}</blockquote>\n"
        f"<b>Input PinYin: </b>\n<blockquote>{result.InputCHPinyin}</blockquote>\n\n"
        f"<b>Reply: </b>\n<blockquote>{result.Reply}</blockquote>\n"
        f"<b>Reply Translation: </b>\n<blockquote>{result.ReplyCH}</blockquote>\n"
        f"<b>Reply PinYin: </b>\n<blockquote>{result.ReplyCHPinyin}</blockquote>"
    )

    return tg_result