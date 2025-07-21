# WEB前端JS Mock服务代码示例与团队规范

## 1. Mock服务具体代码示例

### 1.1 Mock Service Worker (msw) 示例
```js
// src/mocks/handlers.js
import { rest } from 'msw';

export const handlers = [
  rest.get('/api/users/:id', (req, res, ctx) => {
    const { id } = req.params;
    return res(
      ctx.status(200),
      ctx.json({ id, name: 'Tom', email: 'tom@test.com' })
    );
  }),
  rest.post('/api/login', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({ token: 'mock-token-123' })
    );
  })
];
```

```js
// src/mocks/browser.js
import { setupWorker } from 'msw';
import { handlers } from './handlers';

export const worker = setupWorker(...handlers);
```

```js
// src/index.js
import { worker } from './mocks/browser';

if (process.env.NODE_ENV === 'development') {
  worker.start();
}
```

### 1.2 Jest集成Mock服务（msw）
```js
// src/setupTests.js
import { server } from './mocks/server';

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

---

## 2. 团队Mock规范

- **接口文档同步**：Mock数据结构应与后端接口文档（如OpenAPI/Swagger）保持一致。
- **目录结构统一**：如 `src/mocks/handlers.js`、`src/mocks/data/`、`src/mocks/server.js`。
- **数据模板复用**：常用Mock数据抽离为模块，便于多接口复用。
- **异常场景覆盖**：每个接口应有正常、异常、超时等多种Mock响应。
- **Mock数据版本管理**：Mock数据随接口变更同步更新，纳入代码评审。
- **Mock切换机制**：支持本地/测试/预发环境灵活切换Mock与真实服务。

---

## 3. Mock与真实服务切换机制

### 3.1 环境变量切换
```js
// src/index.js
if (process.env.REACT_APP_USE_MOCK === 'true') {
  worker.start();
}
```
- 通过 `.env` 文件配置 `REACT_APP_USE_MOCK=true/false` 实现切换。

### 3.2 运行时切换（如URL参数、配置中心）
- 支持通过URL参数（如`?mock=true`）或远程配置动态切换Mock。
- 关键代码示例：
```js
const useMock = window.location.search.includes('mock=true');
if (useMock) {
  worker.start();
}
```

---

## 4. Mock在CI/CD中的集成实践

- **自动化测试**：CI流程中始终启用Mock服务，保证测试环境数据可控、可复现。
- **接口变更检测**：集成接口契约测试（如Swagger diff），Mock数据与接口文档自动对比。
- **Mock数据快照**：测试通过后保存Mock响应快照，便于回归测试。
- **多环境Mock**：支持本地、CI、预发等多环境Mock配置，避免真实数据污染。
- **CI配置示例（GitHub Actions）**：
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Use Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run test # 测试时自动启用Mock服务
```

---

## 5. 总结
- Mock服务代码应模块化、易维护，支持多场景切换。
- 团队应建立Mock数据规范、切换机制和CI集成流程，保障开发与测试效率。
- Mock与真实服务的无缝切换是现代前端工程的重要能力。 