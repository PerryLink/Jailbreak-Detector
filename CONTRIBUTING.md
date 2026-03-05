# Contributing to Jailbreak Detector

# 为 Jailbreak Detector 做贡献

Thank you for your interest in contributing to Jailbreak Detector!

感谢你对 Jailbreak Detector 项目的关注！

---

## 📌 Project Status | 项目状态

This is currently a **personal project** maintained by [@PerryLink](https://github.com/PerryLink). While contributions are welcome, please note that this project is primarily developed and maintained by a single person.

这是一个**个人维护项目**，由 [@PerryLink](https://github.com/PerryLink) 维护。虽然欢迎贡献，但请注意这个项目主要由一个人开发和维护。

---

## 🐛 Reporting Issues | 报告问题

If you find a bug or have a feature request, please open an issue on GitHub:

如果你发现了 bug 或有功能建议，请在 GitHub 上提交 issue：

1. Check if the issue already exists | 检查问题是否已存在
2. Use a clear and descriptive title | 使用清晰描述性的标题
3. Provide detailed information: | 提供详细信息：
   - Steps to reproduce | 复现步骤
   - Expected behavior | 期望行为
   - Actual behavior | 实际行为
   - Environment details (OS, Python version) | 环境详情（操作系统、Python 版本）

---

## 💻 Development Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python 3.8 or higher | Python 3.8 或更高版本
- Git

### Setup Steps | 搭建步骤

1. **Fork and clone the repository | Fork 并克隆仓库**

```bash
git clone https://github.com/YOUR_USERNAME/jailbreak-detector.git
cd jailbreak-detector
```

2. **Create a virtual environment | 创建虚拟环境**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies | 安装依赖**

```bash
pip install -e ".[dev]"
```

4. **Run tests to verify setup | 运行测试验证安装**

```bash
pytest tests/ -v
```

---

## 📝 Code Standards | 代码规范

This project follows **PEP 8** style guidelines.

本项目遵循 **PEP 8** 代码风格规范。

### Formatting | 代码格式化

Use Black for code formatting | 使用 Black 格式化代码:

```bash
black src/ tests/
```

### Linting | 代码检查

Use Ruff for linting | 使用 Ruff 进行代码检查:

```bash
ruff check src/ tests/
```

### Testing | 测试

- Write tests for new features | 为新功能编写测试
- Ensure all tests pass before submitting | 提交前确保所有测试通过
- Aim for high test coverage | 追求高测试覆盖率

```bash
pytest tests/ -v --cov=jailbreak_detector
```

---

## 🔄 Pull Request Process | 提交 Pull Request 流程

1. **Create a new branch | 创建新分支**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes | 进行修改**
   - Write clean, readable code | 编写清晰可读的代码
   - Follow PEP 8 guidelines | 遵循 PEP 8 规范
   - Add tests for new functionality | 为新功能添加测试
   - Update documentation if needed | 如需要更新文档

3. **Format and test your code | 格式化和测试代码**

```bash
black src/ tests/
ruff check src/ tests/
pytest tests/ -v
```

4. **Commit your changes | 提交更改**

```bash
git add .
git commit -m "feat: add your feature description"
```

Use conventional commit messages | 使用约定式提交信息:
- `feat:` - New feature | 新功能
- `fix:` - Bug fix | Bug 修复
- `docs:` - Documentation changes | 文档更改
- `test:` - Test additions or changes | 测试添加或更改
- `refactor:` - Code refactoring | 代码重构
- `style:` - Code style changes | 代码风格更改

5. **Push to your fork | 推送到你的 fork**

```bash
git push origin feature/your-feature-name
```

6. **Open a Pull Request | 创建 Pull Request**
   - Provide a clear description of changes | 提供清晰的更改描述
   - Reference any related issues | 引用相关的 issue
   - Wait for review | 等待审查

---

## 🎯 Development Guidelines | 开发指南

### Adding New Patterns | 添加新模式

To add new jailbreak patterns | 添加新的越狱模式:

1. Edit `data/patterns.json` | 编辑 `data/patterns.json`
2. Add patterns to appropriate category | 将模式添加到适当的类别
3. Test the new patterns | 测试新模式
4. Document the patterns if needed | 如需要记录模式

### Code Organization | 代码组织

- Keep functions small and focused | 保持函数小而专注
- Use type hints where appropriate | 适当使用类型提示
- Write docstrings for public APIs | 为公共 API 编写文档字符串
- Avoid unnecessary complexity | 避免不必要的复杂性

---

## 📞 Questions? | 有问题？

If you have questions about contributing, feel free to:

如果你对贡献有疑问，可以：

- Open an issue for discussion | 开启 issue 讨论
- Contact the maintainer: novelnexusai@outlook.com | 联系维护者：novelnexusai@outlook.com

---

## 📜 License | 许可证

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

通过贡献，你同意你的贡献将在 Apache License 2.0 下授权。

---

Thank you for contributing! | 感谢你的贡献！
