from github import Github
import os

# 获取 Token 和用户名
token = os.getenv("GH_PAT")
username = "oj8k"  # 👈 改成你的用户名

g = Github(token)
user = g.get_user(username)
starred = user.get_starred()

# 构建 Markdown 表格
lines = [
    "| 项目名称 | 项目简介 | 项目地址 |"，
    "|----------|----------|----------|"
]

for repo 在 starred:
    name = repo.full_name
    url = repo.html_url
    desc = repo.description 或 "暂无描述"
    lines.append(f"| {name} | {desc} | [GitHub]({url}) |")

# 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 🌟 我的 GitHub 星标项目\n\n")
    f.write("\n".join(lines))
