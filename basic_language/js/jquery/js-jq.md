让我详细解释 jQuery、JavaScript 和 document 之间的区别和关系：

## 1. JavaScript (原生 JavaScript)

### 基本概念
- **JavaScript** 是一种编程语言
- 是浏览器原生支持的脚本语言
- 可以直接操作 DOM、处理事件、发送 AJAX 请求等

### 原生 JavaScript 示例
```javascript
// DOM 选择
document.getElementById('myId');
document.querySelector('.myClass');
document.querySelectorAll('p');

// 事件绑定
document.getElementById('button').addEventListener('click', function() {
    console.log('按钮被点击');
});

// 样式操作
document.getElementById('element').style.color = 'red';
document.getElementById('element').classList.add('active');

// AJAX 请求
fetch('/api/data')
    .then(response => response.json())
    .then(data => console.log(data));
```

## 2. Document 对象

### 基本概念
- **Document** 是 JavaScript 的内置对象
- 代表整个 HTML 文档
- 是 DOM 树的根节点
- 提供了访问和操作页面元素的方法

### Document 对象的方法
```javascript
// 元素选择
document.getElementById('myId');           // 通过 ID 选择
document.getElementsByClassName('cls');   // 通过类名选择
document.getElementsByTagName('div');     // 通过标签名选择
document.querySelector('.myClass');       // CSS 选择器
document.querySelectorAll('p');           // 选择所有匹配元素

// 创建元素
document.createElement('div');
document.createTextNode('文本内容');

// 文档信息
document.title = '新标题';
document.URL;
document.domain;
```

## 3. jQuery

### 基本概念
- **jQuery** 是一个 JavaScript 库
- 基于 JavaScript 构建，简化了 DOM 操作
- 提供了跨浏览器兼容的 API
- 使用 `$` 符号作为主要标识符

### jQuery 示例
```javascript
// DOM 选择
$('#myId');           // 等同于 document.getElementById('myId')
$('.myClass');        // 等同于 document.querySelectorAll('.myClass')
$('p');               // 选择所有 p 标签

// 事件绑定
$('#button').click(function() {
    console.log('按钮被点击');
});

// 样式操作
$('#element').css('color', 'red');
$('#element').addClass('active');

// AJAX 请求
$.get('/api/data', function(data) {
    console.log(data);
});
```

## 4. 三者关系对比

### 层次关系
```
JavaScript (语言)
    ↓
Document (内置对象)
    ↓
jQuery (第三方库)
```

### 功能对比表

| 功能 | JavaScript | Document | jQuery |
|------|------------|----------|---------|
| 元素选择 | `document.getElementById()` | `document.getElementById()` | `$('#id')` |
| 事件绑定 | `addEventListener()` | `addEventListener()` | `.click()` |
| 样式操作 | `element.style` | `element.style` | `.css()` |
| 类操作 | `classList` | `classList` | `.addClass()` |
| AJAX | `fetch()` | 无 | `$.ajax()` |

## 5. 具体代码对比

### 元素选择
```javascript
// JavaScript + Document
var element = document.getElementById('myId');
var elements = document.querySelectorAll('.myClass');

// jQuery
var $element = $('#myId');
var $elements = $('.myClass');
```

### 事件处理
```javascript
// JavaScript + Document
document.getElementById('button').addEventListener('click', function() {
    console.log('点击');
});

// jQuery
$('#button').click(function() {
    console.log('点击');
});
```

### 样式操作
```javascript
// JavaScript + Document
document.getElementById('element').style.color = 'red';
document.getElementById('element').classList.add('active');

// jQuery
$('#element').css('color', 'red');
$('#element').addClass('active');
```

### 内容操作
```javascript
// JavaScript + Document
document.getElementById('element').textContent = '新文本';
document.getElementById('element').innerHTML = '<span>HTML</span>';

// jQuery
$('#element').text('新文本');
$('#element').html('<span>HTML</span>');
```

## 6. 优缺点对比

### JavaScript + Document
**优点:**
- 原生支持，无需额外库
- 性能更好
- 文件体积小
- 完全控制

**缺点:**
- 代码冗长
- 跨浏览器兼容性需要手动处理
- 需要更多样板代码

### jQuery
**优点:**
- 代码简洁
- 跨浏览器兼容性好
- 丰富的插件生态
- 链式调用

**缺点:**
- 需要引入库文件
- 性能相对较低
- 文件体积较大
- 对原生 API 的抽象

## 7. 使用建议

### 何时使用原生 JavaScript
- 简单的 DOM 操作
- 性能要求高的场景
- 现代浏览器环境
- 项目体积要求严格

### 何时使用 jQuery
- 复杂的 DOM 操作
- 需要跨浏览器兼容
- 快速原型开发
- 遗留项目维护

## 8. 现代趋势

随着现代浏览器的发展，原生 JavaScript 的能力越来越强：

```javascript
// 现代 JavaScript 已经可以做到 jQuery 的简洁性
document.querySelector('.myClass').addEventListener('click', e => {
    e.target.classList.add('active');
});

// 使用现代 API
fetch('/api/data')
    .then(response => response.json())
    .then(data => console.log(data));
```

总结：JavaScript 是语言，Document 是内置对象，jQuery 是基于 JavaScript 的库。选择哪种方式取决于项目需求和开发环境。