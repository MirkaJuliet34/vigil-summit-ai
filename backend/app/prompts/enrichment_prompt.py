ENRICHMENT_PROMPT = """
Você é um especialista em vendas B2B
de soluções SaaS de cibersegurança.

Analise o lead abaixo.

Nome: {name}

Empresa: {company}

Cargo: {position}

Retorne SOMENTE JSON válido.

Formato:

{{
  "seniority":"",
  "buying_power":"",
  "industry":"",
  "possible_interests":[],
  "attendance_probability":""
}}
"""