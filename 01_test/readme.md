---
date: 2022-12-08
autoer: 杨逸韬
---

根据三电极栅极放电的简单模型进行学习和测试，顺序为

```
vsim_test.sdf       # 几何和边界条件
vsim_test_bound.sdf # 加边界条件
vsim_test_ptc.sdf   # 加粒子模型
```

没有修改`.pre`代码，都是通过图形化界面的设置完成的.
