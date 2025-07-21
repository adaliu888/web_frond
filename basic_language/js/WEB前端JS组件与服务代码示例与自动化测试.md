# WEB前端JS组件与服务代码示例与自动化测试

## 1. 典型组件代码示例

### 1.1 通用Button组件（React）
```jsx
// Button.tsx
import React from 'react';

type ButtonProps = {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  type?: 'button' | 'submit' | 'reset';
};

export const Button: React.FC<ButtonProps> = ({ children, onClick, disabled, type = 'button' }) => (
  <button type={type} onClick={onClick} disabled={disabled} className="btn">
    {children}
  </button>
);
```

### 1.2 组件单元测试（Jest + React Testing Library）
```js
// Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

test('renders button and handles click', () => {
  const handleClick = jest.fn();
  render(<Button onClick={handleClick}>Click Me</Button>);
  const btn = screen.getByText('Click Me');
  fireEvent.click(btn);
  expect(handleClick).toHaveBeenCalled();
});
```

---

## 2. 典型服务层代码示例

### 2.1 用户服务（TypeScript + Axios）
```ts
// userService.ts
import axios from 'axios';

export interface User {
  id: string;
  name: string;
  email: string;
}

export const getUser = async (id: string): Promise<User> => {
  const res = await axios.get(`/api/users/${id}`);
  return res.data;
};
```

### 2.2 服务单元测试（Jest）
```ts
// userService.test.ts
import axios from 'axios';
import { getUser } from './userService';

jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>;

test('getUser fetches user data', async () => {
  mockedAxios.get.mockResolvedValue({ data: { id: '1', name: 'Tom', email: 'tom@test.com' } });
  const user = await getUser('1');
  expect(user.name).toBe('Tom');
});
```

---

## 3. 自动化测试与CI/CD集成建议

### 3.1 自动化测试
- 单元测试：Jest、Mocha、Vitest
- 组件测试：React Testing Library、Vue Test Utils
- 集成测试：Cypress、Playwright
- 代码覆盖率：nyc、coverage、Codecov
- Mock服务：msw、Mock Service Worker

### 3.2 CI/CD集成建议
- 常用平台：GitHub Actions、GitLab CI、Jenkins、CircleCI
- 典型流程：
  1. 代码提交（push/PR）触发流水线
  2. 安装依赖、静态检查（ESLint/Prettier/TypeCheck）
  3. 运行单元/集成测试，生成覆盖率报告
  4. 构建产物（build）
  5. 自动部署到测试/生产环境
- 关键建议：
  - 测试必须通过才可合并/上线
  - 代码覆盖率达标（如80%+）
  - 自动化部署减少人为失误

---

## 4. 总结
- 组件与服务应配套单元测试，保证功能正确性与可维护性。
- 建议团队持续集成自动化测试与部署，提升交付效率与质量。
- 代码示例、测试用例和CI/CD流程应纳入团队开发规范。 