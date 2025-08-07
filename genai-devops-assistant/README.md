# 🤖 GenAI DevOps Assistant (Slackbot + LLM + DevOps API Integration)

A smart DevOps Assistant powered by GPT-4 / LLaMA, integrated with Slack, GitHub, Jenkins, Kubernetes, and Prometheus. Built using LangChain + FastAPI.

## 🚀 Features

✅ Slack chatbot with natural language interface  
✅ Explains CI/CD errors from Jenkins or GitHub Actions  
✅ Summarizes system metrics from Prometheus & Grafana  
✅ Answers queries about Kubernetes pod status, logs  
✅ Uses FAISS vector DB for semantic search on logs/YAMLs  
✅ Built-in CI/CD, containerized, and self-hostable  

## 🧠 Prompt Examples

- "Why did my last Jenkins job fail?"
- "Show CPU usage of prod cluster."
- "Get logs for video-service pod."
- "Explain this Helm error."

## 🛠️ Stack

| Layer      | Tools Used |
|------------|------------|
| GenAI      | OpenAI GPT-4 / LLaMA + LangChain |
| Backend    | Python + FastAPI |
| Chat       | Slackbot |
| CI/CD      | GitHub Actions, Jenkins |
| Infra      | Docker, Terraform (optional), K8s |
| Monitoring | Prometheus, Grafana |
| Vector DB  | FAISS |
| DevOps     | GitHub + Jenkins APIs |

## 📸 Screenshots & Demos

![Architecture](docs/architecture.png)  
![Demo](docs/demo.gif)

## 🧪 Local Setup

```bash
git clone https://github.com/<your-username>/genai-devops-assistant.git
cd genai-devops-assistant
cp docker/.env.example docker/.env
docker-compose up --build
```

## 🐳 Dockerized Environment

```bash
docker-compose up --build
```

## 🚧 Roadmap

- [x] Slack + LangChain agent
- [x] Jenkins/GitHub integration
- [x] Prometheus/Grafana integration
- [ ] ArgoCD support
- [ ] Voice input (Whisper)
- [ ] Natural language to YAML

## 🤝 Contributing

PRs welcome. Create issues for enhancements or bugs.

## 📄 License

MIT
