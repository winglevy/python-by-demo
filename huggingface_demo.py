from transformers import pipeline

# 初始化情感分析管道
def initialize_sentiment_pipeline():
    """
    初始化Hugging Face的情感分析管道
    """
    # 使用预训练模型 "distilbert-base-uncased-finetuned-sst-2-english" 进行情感分析
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    return pipeline("sentiment-analysis", model=model_name)

# 情感分析函数
def analyze_sentiment(text, pipeline):
    """
    使用管道对文本进行情感分析
    """
    # 使用管道对输入文本进行预测
    result = pipeline(text)
    return result

# 主函数
def main():
    # 初始化情感分析管道
    sentiment_pipeline = initialize_sentiment_pipeline()

    # 输入示例文本
    sample_text = "I really enjoyed this movie! The acting was fantastic."

    # 进行情感分析
    sentiment_result = analyze_sentiment(sample_text, sentiment_pipeline)

    # 打印结果
    print(f"Text: {sample_text}")
    print(f"Sentiment: {sentiment_result[0]['label']} (Score: {sentiment_result[0]['score']:.2f})")

# 运行主程序
if __name__ == "__main__":
    main()
