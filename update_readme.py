from github import Github, Auth
import os

# 获取 Token 和用户名
token = os.getenv("GH_TOKEN")
if not token:
    raise ValueError("GH_TOKEN 环境变量未设置或为空")

auth = Auth.Token(token)
g = Github(auth=auth)

username = "oj8k"
user = g.get_user(username)
starred = user.get_starred()

# GitHub 图标
GITHUB_ICON = '<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="16">'

def format_stars(count):
    return f"{GITHUB_ICON} {count/1000:.1f}K" if count >= 1000 else f"{GITHUB_ICON} {count}"

def wrap_name(name, max_len=20):
    return "<br>".join([name[i:i+max_len] for i in range(0, len(name), max_len)])

def clean_description(desc):
    return (desc or "暂无描述").replace("|", "｜").replace("\n", " ").strip()

# 构建 HTML 表格
lines = [
    "<table>",
    "<thead><tr>",
    "<th style='width:18%; font-size:13px;'>项目名称</th>",
    "<th style='width:42%; font-size:13px;'>项目简介</th>",
    "<th style='width:10%; font-size:13px;'>Star</th>",
    "<th style='width:15%; font-size:13px;'>更新时间</th>",
    "<th style='width:15%; font-size:13px;'>链接</th>",
    "</tr></thead>",
    "<tbody>"
]

for repo in starred:
    name = wrap_name(repo.name)
    url = repo.html_url
    desc = clean_description(repo.description)
    stars = format_stars(repo.stargazers_count)
    updated = repo.updated_at.strftime("%Y-%m-%d")

    lines.append(
        f"<tr>"
        f"<td style='word-break:break-word; max-width:120px; font-size:13px;'>{name}</td>"
        f"<td style='word-break:break-word; max-width:300px; font-size:13px;'>{desc}</td>"
        f"<td style='font-size:13px;'>{stars}</td>"
        f"<td style='font-size:13px;'>{updated}</td>"
        f"<td style='font-size:13px;'><a href='{url}'>GitHub</a></td>"
        f"</tr>"
    )

lines.append("</tbody></table>")

# 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 🌟 我的 GitHub 星标项目\n\n")
    f.write("\n".join(lines))
