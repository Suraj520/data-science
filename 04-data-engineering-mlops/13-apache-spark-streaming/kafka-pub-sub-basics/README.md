#### Kafka
1. Scenario - There are multiple source system and multiple target system and they have to exchange data(messages). They do this via queues but since queue is present on single system so it's efficiency is decreased.
2. Kafka is an open-source distributed event streaming platform that is used to handle real-time data feeds. 
3. It is particularly useful for large-scale data processing where data is collected from multiple disparate sources and needs to be processed quickly and efficiently in real-time. 
4. Kafka provides a fault-tolerant architecture that can handle large volumes of data and supports high throughput and low latency processing. 
It is commonly used to build systems in industries such as finance, healthcare, and e-commerce, where real-time data processing is critical for making quick decisions.
It has a topic, a consumer who consume data based on topic and a producer who produces data. Each data is split into partitions.