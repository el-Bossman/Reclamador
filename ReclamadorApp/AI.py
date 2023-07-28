import openai

openai.api_key = "Tu-Api-Key"





def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def PromptGenerator(remitente, destinatario, contexto, genero, emocion, extension ):
    prompt = f"""
    1. estos son los datos de entrada en 3 comillas simples:
    - remitente:          ```{remitente} ```
    - destinatario:     ```{destinatario} ```
    - contexto:          ```{contexto} ```
    - genero:          ```{genero} ```
    - extension:          ```{extension} ```
    - Emoción:          ```{emocion} ```
    
    2.Imagina que estás escribiendo una carta formal para expresar tu Emoción con respecto a un incidente reciente.
    recuerda que al redactar un reclamo, es importante ser claro, objetivo y respetuoso para maximizar las posibilidades de obtener una respuesta satisfactoria a tu reclamo.
    
    3.¡IMPORTANTE¡ Antes de redactar ten en cuenta la {extension} de caracteres y utliza MAXIMO {extension} caracteres.
    
    4. Utiliza el sentimiento de Emoción como tono para redactar la carta. Asegúrate de comunicar claramente tus sentimientos y explicar las razones detrás 
    de tu Emoción. No utilices directamente la palabra Emoción, sino que busca expresar el tono emocional a través del contenido de la carta.
    
    5. Si no entiendes el reclamo escibe unicamente 
    "Lo siento, parece que no comprendí completamente tu reclamo. Por favor, inténtalo nuevamente para que pueda ayudarte de la mejor manera posible.
    Si puedes proporcionar más detalles o ser más específico, estaré encantado de responder a tu solicitud con mayor precisión. "

    6. Al final de la carta, incluye una línea para firmar como se muestra a continuación:
    <p class="signature">_________________________</p>
   {remitente}
   
    7. no pongas un titulo a la carta.
    FORMATO DE SALIDA div en html
    """
   
    response = get_completion(prompt)
    return response