<script setup lang="ts">
import { Button } from 'ant-design-vue'
import type { Message } from './Message'
import { useSearch } from './api-request.js'

const messages = defineModel<Message[]>('messages')
const msg = defineModel()

async function onSend(event: MouseEvent) {
  const newMsg: Message = {
    type: 'Q',
    text: String(msg.value),
  }
  messages.value?.push(newMsg)

  const { data, error } = await useSearch(msg.value)
  msg.value = ''
  console.log(data)

  const resMsg: Message = {
    type: 'A',
    text: String(data.value.text),
  }
  messages.value?.push(resMsg)
}
</script>

<template>
  <div class="chatArea">
    <div class="chatInput"><a-input v-model:value="msg" @pressEnter="onSend" /></div>
    <Button @click="onSend">Send</Button>
  </div>
</template>

<style scoped>
.chatArea {
  display: inline-block;
  width: 65vw;
}
.chatInput {
  display: inline-block;
  width: calc(65vw - 65px);
}
</style>
