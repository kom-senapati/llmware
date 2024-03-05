"""Global Default Configs for Models, Finetune Wrappers and Prompt Instructions Catalog.

These configs generally do not need to be accessed directly, but can be viewed and updated through
ModelCatalog and PromptCatalog classes.
"""

global_model_repo_catalog_list = [

  # embedding models - direct pull from llmware repo - deprecated for HF pull
  {"model_name": 'mini-lm-sbert-llmware', "display_name": "mini-lm-sbert-llmware", "model_family": "LLMWareSemanticModel",
   "model_category": "embedding", "model_location": "llmware_repo", "embedding_dims": 384, "context_window": 512,
   "link": "", "custom_model_files": [], "custom_model_repo": ""},

  {"model_name": 'industry-bert-insurance-llmware', "display_name": "industry-bert-insurance-llmware",
   "model_family": "LLMWareSemanticModel",
   "model_category": "embedding", "model_location": "llmware_repo", "embedding_dims": 768, "context_window": 512,
   "link": "https://huggingface.co/llmware/industry-bert-insurance-v0.1", "custom_model_files": [],
   "custom_model_repo": "",
   "hf_repo": "llmware/industry-bert-insurance-v0.1"},

  {"model_name": 'industry-bert-contracts-llmware', "display_name": "industry-bert-contracts-llmware",
   "model_family": "LLMWareSemanticModel",
   "model_category": "embedding", "model_location": "llmware_repo", "embedding_dims": 768, "context_window": 512,
   "link": "https://huggingface.co/llmware/industry-bert-contracts-v0.1", "custom_model_files": [],
   "custom_model_repo": "",
   "hf_repo": "llmware/industry-bert-contracts-v0.1"},

  {"model_name": 'industry-bert-asset-management-llmware', "display_name": "industry-bert-asset-management-llmware",
   "model_family": "LLMWareSemanticModel", "model_category": "embedding", "model_location": "llmware_repo",
   "embedding_dims": 768, "context_window": 512,
   "link": "https://huggingface.co/llmware/industry-bert-asset-management-v0.1", "custom_model_files": [],
   "custom_model_repo": "",
   "hf_repo": "llmware/industry-bert-asset-management-v0.1"},

  {"model_name": 'industry-bert-sec-llmware', "display_name": "industry-bert-sec-llmware", "model_family": "LLMWareSemanticModel",
   "model_category": "embedding", "model_location": "llmware_repo", "embedding_dims": 768, "context_window": 512,
   "link": "https://huggingface.co/llmware/industry-bert-sec-v0.1", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "llmware/industry-bert-sec-v0.1"},

    # embedding models

    {"model_name": "all-MiniLM-L6-v2", "display_name": "mini-lm-sbert", "model_family": "HFEmbeddingModel",
     "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 384, "context_window": 512,
     "link": "https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "sentence-transformers/all-MiniLM-L6-v2"},

    {"model_name": 'all-mpnet-base-v2', "display_name": "mpnet-base", "model_family": "HFEmbeddingModel",
     "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 768, "context_window": 514,
     "link": "https://huggingface.co/sentence-transformers/all-mpnet-base-v2",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "sentence-transformers/all-mpnet-base-v2"},

  {"model_name": 'industry-bert-insurance', "display_name": "industry-bert-insurance",
      "model_family": "HFEmbeddingModel",
      "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 768, "context_window":512,
      "link": "https://huggingface.co/llmware/industry-bert-insurance-v0.1", "custom_model_files":[],
      "custom_model_repo": "",
      "hf_repo": "llmware/industry-bert-insurance-v0.1"},

     {"model_name": 'industry-bert-contracts', "display_name": "industry-bert-contracts",
      "model_family": "HFEmbeddingModel",
      "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 768, "context_window":512,
      "link": "https://huggingface.co/llmware/industry-bert-contracts-v0.1", "custom_model_files":[],
      "custom_model_repo": "",
      "hf_repo": "llmware/industry-bert-contracts-v0.1"},

    {"model_name": 'industry-bert-asset-management', "display_name": "industry-bert-asset-management",
      "model_family": "HFEmbeddingModel", "model_category": "embedding", "model_location": "hf_repo",
      "embedding_dims": 768, "context_window":512,
      "link": "https://huggingface.co/llmware/industry-bert-asset-management-v0.1", "custom_model_files":[],
      "custom_model_repo": "",
      "hf_repo": "llmware/industry-bert-asset-management-v0.1"},

     {"model_name": 'industry-bert-sec', "display_name": "industry-bert-sec", "model_family": "HFEmbeddingModel",
      "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 768, "context_window":512,
      "link": "https://huggingface.co/llmware/industry-bert-sec-v0.1", "custom_model_files": [], "custom_model_repo": "",
      "hf_repo": "llmware/industry-bert-sec-v0.1"},

  {"model_name": 'nomic-ai/nomic-embed-text-v1', "display_name": "nomic-text-v1",
   "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 768, "context_window": 8192,
   "link": "https://huggingface.co/nomic-ai/nomic-embed-text-v1", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "nomic-ai/nomic-embed-text-v1"},

  {"model_name": 'jinaai/jina-embeddings-v2-base-en', "display_name": "jina-base-en-v2",
   "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 768, "context_window": 8192,
   "link": "https://huggingface.co/jinaai/jina-embeddings-v2-base-en", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "jinaai/jina-embeddings-v2-base-en"},

  {"model_name": 'jinaai/jina-embeddings-v2-small-en', "display_name": "jina-small-en-v2",
   "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 512, "context_window": 8192,
   "link": "https://huggingface.co/jinaai/jina-embeddings-v2-small-en", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "jinaai/jina-embeddings-v2-small-en"},

  {"model_name": 'BAAI/bge-small-en-v1.5', "display_name": "bge-small-en-v1.5", "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 384, "context_window": 512,
   "link": "https://huggingface.co/BAAI/bge-small-en-v1.5", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "BAAI/bge-small-en-v1.5"},

  {"model_name": 'BAAI/bge-large-en-v1.5', "display_name": "bge-large-en-v1.5", "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 1024, "context_window": 512,
   "link": "https://huggingface.co/BAAI/bge-large-en-v1.5", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "BAAI/bge-large-en-v1.5"},

  {"model_name": 'BAAI/bge-base-en-v1.5', "display_name": "bge-base-en-v1.5", "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 768, "context_window": 512,
   "link": "https://huggingface.co/BAAI/bge-base-en-v1.5", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "BAAI/bge-base-en-v1.5"},

 {"model_name": "thenlper/gte-small", "display_name": "gte-small",
   "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 384, "context_window": 512,
   "link": "https://huggingface.co/thenlper/gte-small", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "thenlper/gte-small"},

  {"model_name": "thenlper/gte-base", "display_name": "gte-base",
   "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 768, "context_window": 512,
   "link": "https://huggingface.co/thenlper/gte-base", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "thenlper/gte-base"},

  {"model_name": "thenlper/gte-large", "display_name": "gte-large",
   "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 1024, "context_window": 512,
   "link": "https://huggingface.co/thenlper/gte-large", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "thenlper/gte-large"},

  {"model_name": 'llmrails/ember-v1', "display_name": "ember-v1",
   "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 1024, "context_window": 512,
   "link": "https://huggingface.co/llmrails/ember-v1", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "llmrails/ember-v1"},

  {"model_name": "WhereIsAI/UAE-Large-V1", "display_name": "uae-large-v1",
   "model_family": "HFEmbeddingModel",
   "model_category": "embedding", "model_location": "hf_repo", "embedding_dims": 1024, "context_window": 512,
   "link": "https://huggingface.co/WhereIsAI/UAE-Large-V1", "custom_model_files": [], "custom_model_repo": "",
   "hf_repo": "WhereIsAI/UAE-Large-V1"},

    # add open ai embeddings
    {"model_name": 'text-embedding-ada-002', "display_name": "OpenAI-Embedding", "model_family": "OpenAIEmbeddingModel",
     "model_category": "embedding", "model_location": "api", "context_window": 8191, "embedding_dims": 1536},

    {"model_name": 'text-embedding-3-small', "display_name": "OpenAI-Embedding", "model_family": "OpenAIEmbeddingModel",
     "model_category": "embedding", "model_location": "api", "context_window": 8191, "embedding_dims": 1536},

    {"model_name": 'text-embedding-3-large', "display_name": "OpenAI-Embedding", "model_family": "OpenAIEmbeddingModel",
     "model_category": "embedding", "model_location": "api", "context_window": 8191, "embedding_dims": 3072},

    # add cohere embeddings
    {"model_name": 'medium', "display_name": "Cohere-Medium-Embedding", "model_family": "CohereEmbeddingModel",
     "model_category": "embedding", "model_location": "api", "context_window": 2048, "embedding_dims": 4096},

    {"model_name": 'xlarge', "display_name": "Cohere-XLarge-Embedding", "model_family": "CohereEmbeddingModel",
     "model_category": "embedding", "model_location": "api", "context_window": 2048, "embedding_dims": 4096},

    # insert new cohere embedding model - v3 - announced first week of November 2023
    {"model_name": 'embed-english-v3.0', "display_name": "Cohere-English-v3", "model_family": "CohereEmbeddingModel",
     "model_category": "embedding", "model_location": "api",  "context_window": 2048, "embedding_dims": 1024},

    {"model_name": 'embed-multilingual-v3.0', "display_name": "Cohere-Multi-Lingual-v3", "model_family": "CohereEmbeddingModel",
     "model_category": "embedding", "model_location": "api", "context_window": 2048, "embedding_dims": 1024},

    {"model_name": 'embed-english-light-v3.0', "display_name": "Cohere-English-v3", "model_family": "CohereEmbeddingModel",
     "model_category": "embedding", "model_location": "api", "context_window": 2048, "embedding_dims": 384},

    {"model_name": 'embed-multilingual-light-v3.0', "display_name": "Cohere-English-v3",
     "model_family": "CohereEmbeddingModel", "model_category": "embedding", "model_location": "api",
     "context_window": 2048, "embedding_dims": 384},

    {"model_name": 'embed-english-v2.0', "display_name": "Cohere-English-v3",
     "model_family": "CohereEmbeddingModel", "model_category": "embedding", "model_location": "api",
     "context_window": 2048, "embedding_dims": 4096},

    {"model_name": 'embed-english-light-v2.0', "display_name": "Cohere-English-v3",
     "model_family": "CohereEmbeddingModel", "model_category": "embedding", "model_location": "api",
     "context_window": 2048, "embedding_dims": 1024},

    {"model_name": 'embed-multilingual-v2.0', "display_name": "Cohere-English-v3",
     "model_family": "CohereEmbeddingModel", "model_category": "embedding", "model_location": "api",
     "context_window": 2048, "embedding_dims": 768},
    # end - new cohere embeddings

    # add google embeddings - textembedding-gecko@001
    {"model_name": 'textembedding-gecko@latest', "display_name": "Google-Embedding", "model_family": "GoogleEmbeddingModel",
     "model_category": "embedding","model_location": "api", "context_window": 4000, "embedding_dims": 768},

    # generative-api models
    {"model_name": 'claude-v1', "display_name": "Anthropic Claude-v1", "model_family": "ClaudeModel",
     "model_category": "generative-api", "model_location": "api",  "context_window": 8000},
    {"model_name": 'claude-instant-v1', "display_name": "claude-instant-1.2", "model_family": "ClaudeModel",
     "model_category": "generative-api","model_location": "api", "context_window": 8000},

    # new Anthropic v3 models

    # please note: we have kept Claude-3 window in model_configs at 8192 - but actual model window is 200K
    #  if you pass a single passage of up to 200K, the model should work OK
    # --the shorter context window of 8192 will be applied as default in Prompt when batching up evidence chunks
    # --this can be configured and over-ridden if you prefer to use the full 200K window

    {"model_name": 'claude-3-opus-20240229', "display_name": "Anthropic-Claude-3-Opus", "model_family": "ClaudeModel",
   "model_category": "generative-api", "model_location": "api", "context_window": 8192},

    {"model_name": 'claude-3-sonnet-20240229', "display_name": "Anthropic-Claude-3-Sonnet", "model_family": "ClaudeModel",
   "model_category": "generative-api", "model_location": "api", "context_window": 8192},

    {"model_name": 'claude-2.1', "display_name": "Anthropic Claude-2.1", "model_family": "ClaudeModel",
    "model_category": "generative-api", "model_location": "api", "context_window": 8192},

    {"model_name": 'claude-2.0', "display_name": "Anthropic Claude-Claude2-.0",
    "model_family": "ClaudeModel", "model_category": "generative-api", "model_location": "api", "context_window": 8192},

   {"model_name": 'command-medium-nightly', "display_name": "Cohere Command Medium", "model_family": "CohereGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 2048},
    {"model_name": 'command-xlarge-nightly', "display_name": "Cohere Command XLarge", "model_family": "CohereGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 2048},

    {"model_name": 'summarize-xlarge', "display_name": "Cohere Summarize Xlarge", "model_family": "CohereGenModel",
     "model_category":"generative-api","model_location": "api", "context_window": 2048},
    {"model_name": 'summarize-medium', "display_name": "Cohere Summarize Medium", "model_family": "CohereGenModel",
     "model_category":"generative-api","model_location": "api", "context_window": 2048},
    {"model_name": 'j2-jumbo-instruct', "display_name": "Jurassic-2-Jumbo-Instruct", "model_family": "JurassicModel",
     "model_category":"generative-api", "model_location": "api", "context_window": 2048},
    {"model_name": 'j2-grande-instruct', "display_name": "Jurassic-2-Grande-Instruct", "model_family": "JurassicModel",
     "model_category":"generative-api","model_location": "api", "context_window": 2048},
    {"model_name": 'text-bison@001', "display_name": "Google Palm", "model_family": "GoogleGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 8192},
    {"model_name": 'chat-bison@001', "display_name": "Google Chat", "model_family": "GoogleGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 8192},
    {"model_name": 'text-davinci-003', "display_name": "GPT3-Davinci", "model_family": "OpenAIGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 4096},
    {"model_name": 'text-curie-001', "display_name": "GPT3-Curie", "model_family": "OpenAIGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 2048},
    {"model_name": 'text-babbage-001', "display_name": "GPT3-Babbage", "model_family": "OpenAIGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 2048},
    {"model_name": 'text-ada-001', "display_name": "GPT3-Ada", "model_family": "OpenAIGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 2048},
    {"model_name": "gpt-3.5-turbo", "display_name": "ChatGPT", "model_family": "OpenAIGenModel",
     "model_category": "generative-api","model_location": "api", "context_window": 4000},

    # gpt-4
    {"model_name": "gpt-4", "display_name": "GPT-4", "model_family": "OpenAIGenModel",
     "model_category": "generative-api", "model_location": "api", "context_window": 8000},

    # gpt-3.5-turbo-instruct
    {"model_name": "gpt-3.5-turbo-instruct", "display_name": "GPT-3.5-Instruct", "model_family": "OpenAIGenModel",
     "model_category": "generative-api", "model_location": "api", "context_window": 4000},

    # gpt-4 model announced in November 2023
    {"model_name": "gpt-4-1106-preview", "display_name": "GPT-4-Turbo-1106", "model_family": "OpenAIGenModel",
     "model_category": "generative-api", "model_location": "api", "context_window": 128000},

    # gpt-3.5 model announced in November 2023
    {"model_name": "gpt-3.5-turbo-1106", "display_name": "GPT-3.5-Turbo-1106", "model_family": "OpenAIGenModel",
     "model_category": "generative-api", "model_location": "api", "context_window": 16385},

    # gpt-4 model announced in January 2024
    {"model_name": "gpt-4-0125-preview", "display_name": "GPT-4-Turbo-0125", "model_family": "OpenAIGenModel",
     "model_category": "generative-api", "model_location": "api", "context_window": 128000},
  
    # gpt-3.5 model announced in January 2024
    {"model_name": "gpt-3.5-turbo-0125", "display_name": "GPT-3.5-Turbo-0125", "model_family": "OpenAIGenModel",
     "model_category": "generative-api", "model_location": "api", "context_window": 16385},

    # generative AIB models - aib-read-gpt - "main model"
    {"model_name": "aib-read-gpt", "display_name": "AIB-READ-GPT", "model_family": "AIBReadGPTModel",
     "model_category": "generative-api", "model_location": "api", "context_window": 2048},

    # base supporting models and components
    {"model_name": "bert", "display_name": "Bert", "model_family": "BaseModel", "model_category": "base",
     "model_location": "llmware_repo"},
    {"model_name": "roberta", "display_name": "Roberta", "model_family": "BaseModel", "model_category": "base",
     "model_location": "llmware_repo"},
    {"model_name": "gpt2", "display_name": "GPT-2", "model_family": "BaseModel", "model_category": "base",
     "model_location": "llmware_repo"},

    # add api-based llmware custom model
    {"model_name": "llmware-inference-server", "display_name": "LLMWare-GPT", "model_family": "LLMWareModel",
     "model_category": "generative-api", "model_location": "api", "context_window": 2048},

    # core llmware bling open source models available in catalog directly
    {"model_name": "llmware/bling-1.4b-0.1", "display_name": "bling-1.4b", "model_family": "HFGenerativeModel",
     "model_category": "generative_local", "model_location": "hf_repo", "context_window": 2048,
     "instruction_following": False, "prompt_wrapper": "human_bot", "temperature": 0.3, "trailing_space":"",
     "link": "https://huggingface.co/llmware/bling-1.4b-0.1",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-1.4b-0.1"},

    {"model_name": "llmware/bling-1b-0.1", "display_name": "bling-1b", "model_family": "HFGenerativeModel",
     "model_category": "generative_local", "model_location": "hf_repo", "context_window": 2048,
     "instruction_following": False, "prompt_wrapper": "human_bot", "temperature": 0.3, "trailing_space": "",
     "link": "https://huggingface.co/llmware/bling-1b-0.1",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-1b-0.1"},

    {"model_name": "llmware/bling-falcon-1b-0.1", "display_name": "bling-falcon-1.3b", "model_family": "HFGenerativeModel",
     "model_category": "generative_local", "model_location": "hf_repo", "context_window": 2048,
     "instruction_following": False, "prompt_wrapper": "human_bot", "temperature": 0.3, "trailing_space": "",
     "link": "https://huggingface.co/llmware/bling-falcon-1b-0.1",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-falcon-1b-0.1"
     },

    {"model_name": "llmware/bling-sheared-llama-1.3b-0.1", "display_name": "bling-sheared-llama-1.3b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/bling-sheared-llama-1.3b-0.1",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-sheared-llama-1.3b-0.1"
     },

    {"model_name": "llmware/bling-red-pajamas-3b-0.1", "display_name": "bling-red-pajamas-3b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/bling-red-pajamas-3b-0.1",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-red-pajamas-3b-0.1"},

    {"model_name": "llmware/bling-sheared-llama-2.7b-0.1", "display_name": "bling-sheared-llama-2.7b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/bling-sheared-llama-2.7b-0.1",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-sheared-llama-2.7b-0.1"},

    {"model_name": "llmware/bling-stable-lm-3b-4e1t-v0", "display_name": "bling-stablelm-3b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/bling-stable-lm-3b-4e1t-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-stable-lm-3b-4e1t-v0"},

    {"model_name": "llmware/bling-cerebras-1.3b-0.1", "display_name": "bling-cerebras-1.3b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/bling-cerebras-1.3b-0.1",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-cerebras-1.3b-0.1"},

    {"model_name": "llmware/bling-tiny-llama-v0", "display_name": "bling-tiny-llama-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/bling-tiny-llama-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/bling-tiny-llama-v0"},

    # create dragon models
    {"model_name": "llmware/dragon-yi-6b-v0", "display_name": "dragon-yi-6b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "\n", "link": "https://huggingface.co/llmware/dragon-yi-6b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/dragon-yi-6b-v0"},

    {"model_name": "llmware/dragon-stablelm-7b-v0", "display_name": "dragon-stablelm-7b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/dragon-stablelm-7b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/dragon-stablelm-7b-v0"},

    {"model_name": "llmware/dragon-mistral-7b-v0", "display_name": "dragon-mistral-7b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/dragon-mistral-7b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/dragon-mistral-7b-v0"},

    {"model_name": "llmware/dragon-red-pajama-7b-v0", "display_name": "dragon-red-pajama-7b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/dragon-red-pajama-7b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/dragon-red-pajama-7b-v0"},

    {"model_name": "llmware/dragon-deci-6b-v0", "display_name": "dragon-deci-6b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/dragon-deci-6b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/dragon-deci-6b-v0"},

    {"model_name": "llmware/dragon-falcon-7b-v0", "display_name": "dragon-falcon-7b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/dragon-falcon-7b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/dragon-falcon-7b-v0"},

    {"model_name": "llmware/dragon-llama-7b-v0", "display_name": "dragon-llama-7b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/dragon-llama-7b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/dragon-llama-7b-v0"},

    {"model_name": "llmware/dragon-deci-7b-v0", "display_name": "dragon-deci-7b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/dragon-deci-7b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/dragon-deci-7b-v0"},

    # gguf models

    # deprecated access to dragon-mistral-7b-gguf -> replaced by dragon-mistral-answer-tool
    {"model_name": "llmware/dragon-mistral-7b-gguf", "display_name": "dragon-mistral-7b-gguf",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "dragon-mistral-7b-q4_k_m.gguf",
     "gguf_repo": "llmware/dragon-mistral-7b-v0",
     "link": "https://huggingface.co/llmware/dragon-mistral-7b-v0",
     "custom_model_files": ["dragon-mistral-7b-q4_k_m.gguf"], "custom_model_repo": "llmware/dragon-mistral-7b-v0"},

    # deprecated access to dragon-llama-7b-gguf -> replaced by dragon-llama-answer-tool
    {"model_name": "llmware/dragon-llama-7b-gguf", "display_name": "dragon-llama-7b-gguf",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "dragon-llama-7b-q4_k_m.gguf",
     "gguf_repo": "llmware/dragon-llama-7b-v0",
     "link": "https://huggingface.co/llmware/dragon-llama-7b-v0",
     "custom_model_files": ["dragon-llama-7b-q4_k_m.gguf"], "custom_model_repo": "llmware/dragon-llama-7b-v0"},

    # deprecated access to dragon-yi-6b-gguf -> replaced by dragon-yi-answer-tool
    {"model_name": "llmware/dragon-yi-6b-gguf", "display_name": "dragon-yi-6b-gguf",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
    "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "\n",
     "gguf_file": "dragon-yi-6b-q4_k_m.gguf",
     "gguf_repo": "llmware/dragon-yi-6b-v0",
     "link": "https://huggingface.co/llmware/dragon-yi-6b-v0",
     "custom_model_files": ["dragon-yi-6b-q4_k_m.gguf"], "custom_model_repo": "llmware/dragon-yi-6b-v0"},

   {"model_name": "dragon-yi-answer-tool", "display_name": "dragon-yi-6b-answer-tool",
    "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
    "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
    "temperature": 0.3, "trailing_space": "\n",
    "gguf_file": "dragon-yi.gguf",
    "gguf_repo": "llmware/dragon-yi-answer-tool",
    "snapshot": True,
    "link": "https://huggingface.co/llmware/dragon-yi-answer-tool",
    "custom_model_files": ["dragon-yi.gguf"], "custom_model_repo": "llmware/dragon-yi-answer-tool"},

   {"model_name": "dragon-llama-answer-tool", "display_name": "dragon-llama-answer-tool",
    "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
    "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
    "temperature": 0.3, "trailing_space": "",
    "gguf_file": "dragon-llama.gguf",
    "gguf_repo": "llmware/dragon-llama-answer-tool",
    "snapshot": True,
    "link": "https://huggingface.co/llmware/dragon-llama-answer-tool",
    "custom_model_files": ["dragon-llama.gguf"], "custom_model_repo": "llmware/dragon-llama-answer-tool"},

   {"model_name": "dragon-mistral-answer-tool", "display_name": "dragon-mistral-answer-tool",
    "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
    "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
    "temperature": 0.3, "trailing_space": "",
    "gguf_file": "dragon-mistral.gguf",
    "gguf_repo": "llmware/dragon-mistral-answer-tool",
    "snapshot": True,
    "link": "https://huggingface.co/llmware/dragon-mistral-answer-tool",
    "custom_model_files": ["dragon-mistral.gguf"], "custom_model_repo": "llmware/dragon-mistral-answer-tool"},

    # selected top HF open source chat models - gguf
    {"model_name": "TheBloke/Llama-2-7B-Chat-GGUF", "display_name": "llama-2-7b-chat-gguf",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": True, "prompt_wrapper": "<INST>",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "llama-2-7b-chat.Q4_K_M.gguf",
     "gguf_repo": "llmware/bonchon",
     "link": "https://huggingface.co/llmware/bonchon",
     "custom_model_files": ["llama-2-7b-chat.Q4_K_M.gguf"], "custom_model_repo": "llmware/bonchon"},

    {"model_name": "TheBloke/OpenHermes-2.5-Mistral-7B-GGUF", "display_name": "openhermes-mistral-7b-gguf",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": True, "prompt_wrapper": "chat_ml",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "openhermes-2.5-mistral-7b.Q4_K_M.gguf",
     "gguf_repo": "llmware/bonchon",
     "link": "https://huggingface.co/llmware/bonchon",
     "custom_model_files": ["openhermes-2.5-mistral-7b.Q4_K_M.gguf"], "custom_model_repo": "llmware/bonchon"},

    {"model_name": "TheBloke/zephyr-7B-beta-GGUF", "display_name": "zephyr-7b-gguf",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": True, "prompt_wrapper": "hf_chat",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "zephyr-7b-beta.Q4_K_M.gguf",
     "gguf_repo": "llmware/bonchon",
     "link": "https://huggingface.co/llmware/bonchon",
     "custom_model_files": ["zephyr-7b-beta.Q4_K_M.gguf"], "custom_model_repo": "llmware/bonchon"},

    {"model_name": "TheBloke/Starling-LM-7B-alpha-GGUF", "display_name": "starling-7b-gguf",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": True, "prompt_wrapper": "open_chat",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "starling-lm-7b-alpha.Q4_K_M.gguf",
     "gguf_repo": "llmware/bonchon",
     "link": "https://huggingface.co/llmware/bonchon",
     "custom_model_files": ["starling-lm-7b-alpha.Q4_K_M.gguf"], "custom_model_repo": "llmware/bonchon"
     },

    # new slim models
    {"model_name": "slim-ner-tool", "display_name": "slim-ner-tool",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "slim-ner.gguf",
     "gguf_repo": "llmware/slim-ner-tool",
     "link": "https://huggingface.co/llmware/slim-ner-tool",
     "custom_model_files": ["slim-ner.gguf"], "custom_model_repo": "llmware/slim-ner-tool",
     # add function call parameters
     "function_call": True,
     "primary_keys": ["people", "location", "organization", "misc"],
     "fc_output_values": [],
     "tokenizer": "llmware/slim-ner",
     "value_zone_markers": {"start": [6024,6796, 3366], "stop": [2033,3108]},
     "marker_tokens": [], "marker_token_lookup": {},
     "function": ["classify"],
     "snapshot": True},

    {"model_name": "slim-sentiment-tool", "display_name": "slim-sentiment-tool",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "slim-sentiment.gguf",
     "gguf_repo": "llmware/slim-sentiment-tool",
     "link": "https://huggingface.co/llmware/slim-sentiment-tool",
     "custom_model_files": ["slim-sentiment.gguf"], "custom_model_repo": "llmware/slim-sentiment-tool",
     # add function call parameters
     "function_call": True,
     "primary_keys": ["sentiment"],
     "fc_output_values": ["positive", "neutral", "negative"],
     "tokenizer": "llmware/slim-sentiment",
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [1066, 22198, 17821],
     "marker_token_lookup": {1066: "positive", 22198: "negative", 17821: "neutral"},
     "function": ["classify"],
     "snapshot": True},

    {"model_name": "slim-emotions-tool", "display_name": "slim-emotions-tool",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "slim-emotions.gguf",
     "gguf_repo": "llmware/slim-emotions-tool",
     "link": "https://huggingface.co/llmware/slim-emotions-tool",
     "custom_model_files": ["slim-emotions.gguf"], "custom_model_repo": "llmware/slim-emotions-tool",
     # add function call parameters
     "function_call": True,
     "primary_keys": ["emotions"],
     "fc_output_values": ["afraid", "anger", "angry", "annoyed", "anticipating", "anxious", "apprehensive",
                          "ashamed", "caring", "confident", "content", "devastated", "disappointed", "disgusted",
                          "embarrassed", "excited", "faithful", "fear", "furious", "grateful", "guilty",
                          "hopeful", "impressed", "jealous", "joy", "joyful", "lonely", "love", "nostalgic",
                          "prepared", "proud", "sad", "sadness", "sentimental", "surprise", "surprised",
                          "terrified", "trusting"],
     "tokenizer": "llmware/slim-emotions",
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [],
     "marker_token_lookup": {},
     "function": ["classify"],
     "snapshot": True},

    {"model_name": "slim-ratings-tool", "display_name": "slim-ratings-tool",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "slim-ratings.gguf",
     "gguf_repo": "llmware/slim-ratings-tool",
     "link": "https://huggingface.co/llmware/slim-ratings-tool",
     "custom_model_files": ["slim-ratings.gguf"], "custom_model_repo": "llmware/slim-ratings-tool",
     # add function call parameters
     "function_call": True,
     "primary_keys": ["rating"],
     "fc_output_values": ["1", "2", "3", "4", "5"],
     "tokenizer": "llmware/slim-ratings",
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [],
     "marker_token_lookup": {},
     "function": ["classify"],
     "snapshot": True},

   {"model_name": "slim-intent-tool", "display_name": "slim-intent-tool",
    "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
    "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
    "temperature": 0.3, "trailing_space": "",
    "gguf_file": "slim-intent.gguf",
    "gguf_repo": "llmware/slim-intent-tool",
    "link": "https://huggingface.co/llmware/slim-intent-tool",
    "custom_model_files": ["slim-intent.gguf"], "custom_model_repo": "llmware/slim-intent-tool",
    "function_call": True,
    "primary_keys": ["intent"],
    "fc_output_values": ["account", "cancel", "complaint", "customer service", "delivery", "feedback",
                         "invoice", "new account", "order", "payments", "refund", "shipping",
                         "subscription", "terminate"],
    "tokenizer": "llmware/slim-intent",
    "value_zone_markers": {"start": [6024, 6796, 3366], "stop": [2033, 3108]},
    "marker_tokens": [],
    "marker_token_lookup": {},
    "function": ["classify"],
    "snapshot": True},

    {"model_name": "slim-nli-tool", "display_name": "slim-nli-tool",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "slim-nli.gguf",
     "gguf_repo": "llmware/slim-nli-tool",
     "link": "https://huggingface.co/llmware/slim-nli-tool",
     "custom_model_files": ["slim-nli.gguf"], "custom_model_repo": "llmware/slim-nli-tool",
     "function_call": True,
     "primary_keys": ["evidence"],
     "fc_output_values": ["supports", "neutral", "contradicts"],
     "tokenizer": "llmware/slim-nli",
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [9996,5924,17821],
     "marker_token_lookup": {9996: "contradicts", 5924: "supports", 17821: "neutral"},
     "function": ["classify"],
     "snapshot": True},

    {"model_name": "slim-topics-tool", "display_name": "slim-topics-tool",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "slim-topics.gguf",
     "gguf_repo": "llmware/slim-topics-tool",
     "link": "https://huggingface.co/llmware/slim-topics-tool",
     "custom_model_files": ["slim-topics.gguf"], "custom_model_repo": "llmware/slim-topics-tool",
     "function_call": True,
     "primary_keys": ["topics"],
     "fc_output_values": [],
     "tokenizer": "llmware/slim-topics",
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [],
     "marker_token_lookup": {},
     "function": ["classify"],
     "snapshot": True},

  {"model_name": "slim-tags-tool", "display_name": "slim-tags-tool",
   "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
   "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
   "temperature": 0.3, "trailing_space": "",
   "gguf_file": "slim-tags.gguf",
   "gguf_repo": "llmware/slim-tags-tool",
   "link": "https://huggingface.co/llmware/slim-tags-tool",
   "custom_model_files": ["slim-tags.gguf"], "custom_model_repo": "llmware/slim-tags-tool",
   "function_call": True,
   "primary_keys": ["tags"],
   "fc_output_values": [],
   "tokenizer": "llmware/slim-tags",
   "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
   "marker_tokens": [],
   "marker_token_lookup": {},
   "function": ["classify"],
   "snapshot": True},

    {"model_name": "slim-sql-tool", "display_name": "slim-sql-tool",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "slim-sql.gguf",
     "gguf_repo": "llmware/slim-sql-tool",
     "fc_output_values": [],
     "link": "https://huggingface.co/llmware/slim-sql-tool",
     "custom_model_files": ["slim-sql.gguf"], "custom_model_repo": "llmware/slim-sql-tool",
     "tokenizer": "llmware/slim-sql-1b-v0",
     "snapshot": True},

    {"model_name": "bling-answer-tool", "display_name": "bling-answer-tool",
     "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "",
     "gguf_file": "bling-answer.gguf",
     "gguf_repo": "llmware/bling-answer-tool",
     "link": "https://huggingface.co/llmware/bling-answer-tool",
     "custom_model_files": ["bling-answer.gguf"], "custom_model_repo": "llmware/bling-answer-tool",
     # add function call parameters
     "tokenizer": "llmware/bling-tiny-llama-1b-v0",
     "snapshot": True},

   {"model_name": "slim-category-tool", "display_name": "slim-category-tool",
    "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
    "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
    "temperature": 0.3, "trailing_space": "",
    "gguf_file": "slim-category.gguf",
    "gguf_repo": "llmware/slim-category-tool",
    "link": "https://huggingface.co/llmware/slim-category-tool",
    "custom_model_files": ["slim-category.gguf"], "custom_model_repo": "llmware/slim-category-tool",
    "function_call": True,
    "primary_keys": ["category"],
    "fc_output_values": ["analyst", "announcements", "bonds", "business", "central bank", "commentary",
                         "commodities", "currencies", "dividend", "earnings", "energy", "entertainment",
                         "financials", "health", "human resources", "legal and regulation", "macroeconomics",
                         "markets", "mergers and acquisitions", "opinion", "politics", "public markets",
                         "science", "sports", "stocks", "tech", "world"],
    "tokenizer": "llmware/slim-category",
    "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
    "marker_tokens": [],
    "marker_token_lookup": {},
    "function": ["classify"],
    "snapshot": True},

    # pytorch slim models start here

    {"model_name": "llmware/slim-intent", "display_name": "slim-intent-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
     "link": "https://huggingface.co/llmware/slim-intent",
     "hf_repo": "llmware/slim-intent",
     "custom_model_files": [""], "custom_model_repo": "",
     "function_call": True,
     "primary_keys": ["intent"],
     "fc_output_values": ["account", "cancel", "complaint", "customer service", "delivery", "feedback",
                          "invoice", "new account", "order", "payments", "refund", "shipping",
                          "subscription", "terminate"],
     "function": ["classify"],
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [1066, 22198, 17821],
     "marker_token_lookup": {1066: "positive", 22198: "negative", 17821: "neutral"},
     },

    {"model_name": "llmware/slim-sentiment", "display_name": "slim-sentiment-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
     "link": "https://huggingface.co/llmware/slim-sentiment",
     "hf_repo": "llmware/slim-sentiment",
     "custom_model_files": [""], "custom_model_repo": "",
     "function_call": True,
     "primary_keys": ["sentiment"],
     "fc_output_values": ["positive", "neutral", "negative"],
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [1066, 22198, 17821],
     "marker_token_lookup": {1066: "positive", 22198: "negative", 17821: "neutral"},
     "function": ["classify"]},

    {"model_name": "llmware/slim-emotions", "display_name": "slim-emotions-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
     "link": "https://huggingface.co/llmware/slim-emotions",
     "hf_repo": "llmware/slim-emotions",
     "custom_model_files": [""], "custom_model_repo": "",
     "function_call": True,
     "primary_keys": ["emotions"],
     "fc_output_values": ["afraid", "anger", "angry", "annoyed", "anticipating", "anxious", "apprehensive",
                          "ashamed", "caring", "confident", "content", "devastated", "disappointed", "disgusted",
                          "embarrassed", "excited", "faithful", "fear", "furious", "grateful", "guilty",
                          "hopeful", "impressed", "jealous", "joy", "joyful", "lonely", "love", "nostalgic",
                          "prepared", "proud", "sad", "sadness", "sentimental", "surprise", "surprised",
                          "terrified", "trusting"],
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [1066, 22198, 17821],
     "marker_token_lookup": {1066: "positive", 22198: "negative", 17821: "neutral"},
     "function": ["classify"]},

    {"model_name": "llmware/slim-ner", "display_name": "slim-ner-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
     "link": "https://huggingface.co/llmware/slim-ner",
     "custom_model_files": [""], "custom_model_repo": "",
     "hf_repo": "llmware/slim-ner",
     "function_call": True,
     "primary_keys": ["person", "organization", "place", "misc"],
     "fc_output_values": [],
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [],
     "marker_token_lookup": {},
     "function": ["classify"]},

    {"model_name": "llmware/slim-nli", "display_name": "slim-nli-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
     "link": "https://huggingface.co/llmware/slim-nli",
     "custom_model_files": [""], "custom_model_repo": "",
     "hf_repo": "llmware/slim-nli",
     "function_call": True,
     "primary_keys": ["evidence"],
     "fc_output_values": ["supports", "neutral", "contradicts"],
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [],
     "marker_token_lookup": {},
     "function": ["classify"]},

    {"model_name": "llmware/slim-ratings", "display_name": "slim-ratings-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
     "link": "https://huggingface.co/llmware/slim-ratings",
     "hf_repo": "llmware/slim-ratings",
     "custom_model_files": [""], "custom_model_repo": "",
     "function_call": True,
     "primary_keys": ["rating"],
     "fc_output_values": ["1", "2", "3", "4", "5"],
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [],
     "marker_token_lookup": {},
     "function": ["classify"]},

    {"model_name": "llmware/slim-category", "display_name": "slim-category-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
     "link": "https://huggingface.co/llmware/slim-category",
     "custom_model_files": [""], "custom_model_repo": "",
     "hf_repo": "llmware/slim-category",
     "function_call": True,
     "primary_keys": ["category"],
     "fc_output_values": ["analyst", "announcements", "bonds", "business", "central bank", "commentary",
                          "commodities", "currencies", "dividend", "earnings", "energy", "entertainment",
                          "financials", "health", "human resources", "legal and regulation", "macroeconomics",
                          "markets", "mergers and acquisitions", "opinion", "politics", "public markets",
                          "science", "sports", "stocks", "tech", "world"],
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [],
     "marker_token_lookup": {},
     "function": ["classify"]},

    {"model_name": "llmware/slim-tags", "display_name": "slim-tags-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
     "link": "https://huggingface.co/llmware/slim-tags",
     "custom_model_files": [""], "custom_model_repo": "",
     "hf_repo": "llmware/slim-tags",
     "function_call": True,
     "value_zone_markers": {"start": [6024, 6796,3366], "stop": [2033, 3108]},
     "marker_tokens": [],
     "marker_token_lookup": {},
     "primary_keys": ["tags"],
     "fc_output_values": [],
     "function": ["classify"]},

   {"model_name": "llmware/slim-topics", "display_name": "slim-topics-1b",
    "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
    "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
    "temperature": 0.3, "trailing_space": "", "gguf_file": "", "gguf_repo": "",
    "link": "https://huggingface.co/llmware/slim-topics",
    "hf_repo": "llmware/slim-topics",
    "custom_model_files": [""], "custom_model_repo": "",
    "function_call": True,
    "value_zone_markers": {"start": [6024, 6796, 3366], "stop": [2033, 3108]},
    "marker_tokens": [],
    "marker_token_lookup": {},
    "primary_keys": ["topics"],
    "fc_output_values": [],
    "function": ["classify"]},

    # sql pytorch model
    {"model_name": "llmware/slim-sql-1b-v0", "display_name": "slim-sql-1b",
     "model_family": "HFGenerativeModel", "model_category": "generative_local", "model_location": "hf_repo",
     "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
     "temperature": 0.3, "trailing_space": "", "link": "https://huggingface.co/llmware/slim-sql-1b-v0",
     "custom_model_files": [], "custom_model_repo": "",
     "hf_repo": "llmware/slim-sql-1b-v0",
     #TODO: assess how to handle SQL models with function call parameters
     "function_call": False,
     "fc_output_values": [],
     "primary_keys": ["sql"], "function": ["sql"]},

  {"model_name": "bling-stablelm-3b-tool", "display_name": "llmware/bling-stablelm-3b-gguf",
  "model_family": "GGUFGenerativeModel", "model_category": "generative_local", "model_location": "llmware_repo",
  "context_window": 2048, "instruction_following": False, "prompt_wrapper": "human_bot",
  "temperature": 0.3, "trailing_space": "",
  "gguf_file": "bling-stablelm.gguf",
  "gguf_repo": "llmware/bling-stablelm-3b-gguf",
  "snapshot": True,
  "link": "https://huggingface.co/llmware/bling-stablelm-3b-gguf",
  "custom_model_files": ["bling-stablelm.gguf"], "custom_model_repo": "llmware/bling-stablelm-3b-gguf"},

]

""" Fine-tuning Prompt Wrappers - virtually all instruct fine-tuned models will have a special 'prompt wrapper' 
that is an artifact from fine-tuning and needs to be applied consistently to lead to the expected model behavior.   
There are a number of common formats captured in the default catalog, but can be extended through ModelCatalog.   
When constructing the prompt, this wrapper will be applied automatically. """

global_model_finetuning_prompt_wrappers_lookup = {

        #   each wrapper can consist of up to 5 elements to represent common segments of the prompt
        #   1.  optional - "system_start" and "system_stop"
        #   2.  required - "main_start" and "main_stop"
        #   3.  required - "start_llm_response"

        "human_bot": {"main_start": "<human>: ", "main_stop": "\n", "start_llm_response": "<bot>:"},

        "<INST>": {"main_start": "<INST>", "main_stop": "</INST>", "start_llm_response": ""},

        "hf_chat": {"system_start": "<|im_start|>system\n", "system_stop": "<|im_end|>\n",
                    "main_start": "<|im_start|>user", "main_stop": "<|im_end|>\n",
                    "start_llm_response": "<|im_start|>assistant"},

        "open_chat": {"main_start": "GPT4 User: ", "main_stop": "<|endofturn|>",
                      "start_llm_response": "GPT4 Assistant:"},

        "alpaca": {"main_start": "### Instruction: ", "main_stop": "\n",
                   "start_llm_response": "### Response: "},

        "chat_ml": {"system_start": "<|im_start|>system", "system_stop":"<|im_end|>\n",
                    "main_start":"<|im_start|>user", "main_stop":"<|im_end|>\n",
                    "start_llm_response":"<|im_start|>assistant"}
        }


""" Global default prompt catalog consists of a set of prebuilt useful prompt instructions across a wide range
of models.   Unlike prompt_wrappers, which tend to be an attribute of the model, the prompt catalog can be invoked
on a 'prompt-by-prompt' basis to drive different behavior from a model.   Note:  not all models will support
 very complex open-ended instructions or respond in a consistent manner. """

global_default_prompt_catalog = [

    {"prompt_name": "just_the_facts",
     "prompt_description": "Closed Context - read passage, answer question, stick to the facts.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the following text: ",
     "blurb2": " Please answer the question: ",
     "instruction": "In providing the answer, please only use facts contained in the text.",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words.",
     "user_vars": {}},

    {"prompt_name": "answer_or_not_found",
     "prompt_description": "Closed Context - read passage, answer question, provide 'Not Found' if no answer in text.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the following text: ",
     "blurb2": " Please answer the question: ",
     "instruction": "Please only use facts in the text.  If the text does not provide the answer, then please "
                    "respond with: {{not_found_response}}",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words.",
     "user_vars": {"not_found_response": "'Not Found.'"}},

    {"prompt_name": "number_or_none",
     "prompt_description": "Closed Context - read passage, answer question, provide 'Not Found' if no answer in text.",
     "run_order": ["blurb1", "$context", "blurb2", "$query","instruction"],
     "blurb1" : "Please read the following text: ",
     "blurb2" : " Please answer the question: ",
     "instruction": "Please provide a specific number as an answer from the text.  "
                    "If the text does not provide a specific numerical answer, then please respond "
                    "with: {{not_found_response}}",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words.",
     "user_vars": {"not_found_response": "'Not Found.'"}},

    {"prompt_name": "summarize_with_bullets",
     "prompt_description": "Basic summarization with open ended number of bullet points.",
     "run_order": ["blurb1", "$context", "instruction"],
     "blurb1": "Please read the following text: ",
     "instruction": "Please summarize with bulletpoints.",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words.",
     "user_vars": {}},

    {"prompt_name": "summarize_with_numbered_bullets",
     "prompt_description": "Summarization with specified number of bullet points.",
     "run_order": ["blurb1", "$context", "instruction"],
     "blurb1": "Please read the following text: ",
     "instruction": "Please summarize the text with approximately {{number_of_bulletpoints}} numbered bulletpoints.",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words.",
     "user_vars": {"number_of_bulletpoints": 5}},

    {"prompt_name": "xsummary",
     "prompt_description": "Xtreme summarization with specified number of words.",
     "run_order": ["blurb1", "$context", "instruction"],
     "blurb1": "Please read the following text: ",
     "instruction": "Please summarize the text in no more than {{number_of_words}} words.",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words.",
     "user_vars": {"number_of_words": 25}},

    {"prompt_name": "completion",
     "prompt_description": "Open context text generation to complete starting point provided in prompt.",
     "run_order": ["blurb1", "$query", "instruction"],
     "blurb1": "Here is the starting point of a longer text: ",
     "instruction": "Please complete this text in the style provided in the text.",
     "system_message": "You are a helpful assistant who is a good creative writer.",
     "user_vars": {}},

    {"prompt_name": "dialog_summary",
     "prompt_description": "General summarization of a conversation text with specified number of bullet points.",
     "run_order": ["blurb1", "$context", "instruction"],
     "blurb1": "Please read the following discussion between two parties: ",
     "instruction": "Please summarize the key points from the conversation using less "
                    "than {{number_of_bulletpoints}} bulletpoints.",
     "system_message": "You are a helpful assistant.",
     "user_vars": {"number_of_bulletpoints": 10}},

    {"prompt_name": "not_found_classifier",
     "prompt_description": "Not Found Response classifier - used to ask a model to classify a particular response "
                           "as 'not found' - very useful in RAG applications.",
     "run_order": ["blurb1", "blurb2", "$context", "instruction"],
     "blurb1": "Here are several examples of a 'not found' response: "
               "Not Found \n"
               "The text does not provide an answer. \n"
               "The answer is not clear. \n"
               "Sorry, I could not find a definitive answer. \n"
               "The answer is not provided in the information given. \n"
               "The text does not specify the answer to this question. \n",
     "blurb2": "Here is a new example: ",
     "instruction": "Please respond 'Yes' or 'No' if this new example is a 'Not Found' response.",
     "system_message": "You are a helpful assistant.",
     "user_vars": {}},

    {"prompt_name": "top_level_select",
     "prompt_description": "Select the best answer among choices provided.",
     "run_order": ["blurb1", "$query", "blurb2","$context", "instruction"],
     "blurb1": "We are trying to answer the following question: ",
     "blurb2": "Which of the following selections best answers the question?",
     "instruction": "Please respond with the best answer among these selections.  "
                    "If more than one answer is useful, please summarize with bulletpoints.",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words.",
     "user_vars": {}},

    {"prompt_name": "answer_question_in_role",
     "prompt_description": "Answer a question with a specific role or point of view.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the following text: ",
     "blurb2": "Please answer the following question: ",
     "instruction": "In providing an answer to the question, please assume the perspective of a {{role}} and "
                    "write in that style.",
     "system_message": "You are a helpful assistant.",
     "user_vars": {"role": "business analyst"}},

    {"prompt_name": "editor_in_role",
     "prompt_description": "Edit a passage with a specific role or point of view.",
     "run_order": ["blurb1", "$context", "instruction"],
     "blurb1": "Please read the following text: ",
     "instruction": "Our task is to edit and improve the language of the text from the perspective of a business analyst.",
     "system_message": "You are a helpful editor and writer who reads text and improves the writing.",
     "user_vars": {"role": "business analyst"}},

    {"prompt_name": "yes_no",
     "prompt_description": "Answer a question with 'Yes' or 'No'.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the following text: ",
     "blurb2": "Based on these materials, please answer the question: ",
     "instruction": "Please answer this question with 'Yes' or 'No'.  If the text does not provide an answer,"
                    "then please respond with 'Not Found.'",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words.",
     "user_vars": {}},

    {"prompt_name": "multiple_choice",
     "prompt_description": "Answer a question using a set of pre-defined choices provided.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the following text: ",
     "blurb2": "Based on these materials, please answer the question: ",
     "instruction": "Please select from the choices provided.  If the text does not provide an answer,"
                    "then please respond with 'Not Found.'",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words."},

    {"prompt_name": "default_with_context",
     "prompt_description": "Default simple prompt when a question and context are passed.",
     "run_order": ["blurb1", "$context", "blurb2", "$query"],
     "blurb1": "Please read the following text: ",
     "blurb2": "Based on this text, please answer the question: ",
     "instruction": "",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words."},

    {"prompt_name": "default_no_context",
     "prompt_description": "Default simple prompt when only a question is passed.",
     "run_order": ["blurb1","$query"],
     "blurb1": "Please discuss the following: ",
     # "blurb2": "Based on this text, please answer the question: ",
     "instruction": "",
     "system_message": "You are a helpful assistant who likes to answer questions."},

    {"prompt_name": "summarize_with_bullets_w_query",
     "prompt_description": "Summarization of a text with a specific question being posed.",
     "run_order": ["blurb1", "$context", "blurb2","$query","instruction"],
     "blurb1": "Please read the following text: ",
     "blurb2": "Please read the following question: ",
     "instruction": "Please summarize with bulletpoints an analysis of the question.",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words."},

    {"prompt_name": "summarize_with_references_w_query",
     "prompt_description": "Summarization with text with guidance to provide reference to specific "
                           "information in the text passage.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the following text: ",
     "blurb2": "Please read the following question: ",
     "instruction": "Please provide an analysis of the question using information and specific clauses "
                    "in the text.",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words."},

    {"prompt_name": "write_poem",
     "prompt_description": "Write a poem prompt - note: results may vary greatly by model.",
     "run_order": ["instruction", "$query"],
     "instruction": "Please write a poem using the following prompt: ",
     "system_message": "You are a helpful assistant who is a creative writer and can rhyme words easily."},

    {"prompt_name": "ten_words",
     "prompt_description": "Xtreme summarization to answer question from a text in 10 words of less.",
     "run_order": ["instruction", "$query", "$context"],
     "blurb1": "Please read the following text: ",
     "blurb2": "Please read the following question: ",
     "instruction": "In no more than ten words, please give concise answer to the following question, using the "
                    "text as evidence to support",
     "system_message": "You are a helpful assistant who speaks with facts and no wasted words."},

    {"prompt_name": "explain_child",
     "prompt_description": "Standard simplified answer prompt - note: results may vary greatly by model.",
     "run_order": ["instruction", "$query", "$context"],
     "instruction": "Please explain to a child the following question using the provided text: ",
     "system_message": "You are a helpful assistant."},

    {"prompt_name": "make_joke",
     "prompt_description": "Standard joke prompt - note:  results may vary greatly by model.",
     "run_order": ["instruction", "$query"],
     "instruction": "Please be funny and tell a joke on the subject of: ",
     "system_message": "You are a helpful assistant with a good sense of humor."},

    {"prompt_name": "tell_story",
     "prompt_description": "Standard tell a story prompt - note: results may vary greatly by model.",
     "run_order": ["instruction", "$query"],
     "instruction": "Please write the start of a story on the topic of: ",
     "system_message": "You are a helpful assistant."},

    {"prompt_name": "write_headline",
     "prompt_description": "Generate a headline from a question and context.",
     "run_order": ["instruction", "$query", "$context"],
     "instruction": "Please write the headline only in a few words in capitalization to answer the question below, "
                    "using the materials provided. ",
     "system_message": "You are a helpful assistant."},

    {"prompt_name": "facts_only",
     "prompt_description": "Basic 'facts only' Q&A prompt.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please use the following materials- ",
     "blurb2": "Please answer the following question - ",
     "instruction": "In answering the question, please only use information contained in the provided materials.",
     "system_message": "You are a helpful assistant."},

    {"prompt_name": "top_bulletpoints",
     "prompt_description": "Summarization with question and answer in 5 bullet points.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the text below -  ",
     "blurb2": "Please read the following question - ",
     "instruction": "Please answer the question using the text, and write no more than 5 bulletpoints.",
     "system_message": "You are a helpful assistant."},

    {"prompt_name": "report_title",
     "prompt_description": "Generate title of report given context passage.",
     "run_order": ["instruction", "$context"],
     "instruction": "Please write the title to a report with the following information:  ",
     "system_message": "You are a helpful assistant."},

    {"prompt_name": "marketing_slogan",
     "prompt_description": "Generate marketing style slogan given context passage.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the following materials- ",
     "blurb2": "Please answer the following question - ",
     "instruction": "Please write a marketing slogan for the following offering using the following information as "
                    "background source materials.",
     "system_message": "You are a helpful assistant."},

    {"prompt_name": "top_level_summary",
     "prompt_description": "Summarization prompt intended for 'second-level' summaries of materials.",
     "run_order": ["blurb1", "$context", "blurb2", "$query", "instruction"],
     "blurb1": "Please read the following materials- ",
     "blurb2": "Please answer the following question - ",
     "instruction": "In answering the question, please write no more than five bulletpoints, and reference the most "
                    "important facts in the source materials.",
     "system_message": "You are a helpful assistant."},

]
