from typing import Optional

from embedchain.helpers.json_serializable import register_deserializable


@register_deserializable
class BaseEmbedderConfig:
    def __init__(
        self,
        model: Optional[str] = None,
        deployment_name: Optional[str] = None,
        vector_dimension: Optional[int] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        """
        Initialize a new instance of an embedder config class.
        :param model: model name of the llm embedding model (not applicable to all providers), defaults to None
        :type model: Optional[str], optional
        :param deployment_name: deployment name for llm embedding model, defaults to None
        :type deployment_name: Optional[str], optional
        :param base_url: Base url the model is hosted under, defaults to "http://localhost:11434"
        :type base_url: Optional[str], optional
        """
        self.model = model
        self.deployment_name = deployment_name
        self.vector_dimension = vector_dimension
        self.api_key = api_key
        self.base_url = base_url or "http://localhost:11434"
