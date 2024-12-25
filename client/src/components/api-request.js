import { ref } from 'vue'
const url = 'http://localhost:8000/api/chat/'

export async function useSearch(question) {
  const data = ref(null)
  const error = ref(null)

  const postData = {
    text: question,
  }
  const options = {
    method: 'POST', // 指定HTTP方法为POST
    headers: {
      'Content-Type': 'application/json', // 设置请求头，指明我们发送的是JSON格式的数据
      // 如果API需要认证，可以在这里添加Authorization头
      // 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    },
    body: JSON.stringify(postData), // 将JavaScript对象转换为JSON字符串
  }

  const res = await fetch(url, options)
  data.value = await res.json()

  return { data, error }
}
