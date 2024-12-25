<script setup lang="ts">
import AnswerItem from './AnswerItem.vue'
import QuestionItem from './QuestionItem.vue'
import type { Message } from './Message'
import { onBeforeUpdate } from 'vue'

const messages = defineModel<Message[]>('messages')
let count = messages.value?.length ? messages.value.length - 1 : 0
onBeforeUpdate(() => {
  count = messages.value?.length ? messages.value.length - 1 : 0
})
</script>

<template>
  <div class="chatHistory" v-for="(msg, index) in messages" :key="index">
    <div v-if="msg.type === 'A'">
      <AnswerItem :text="msg.text" />
    </div>
    <div v-else-if="msg.type === 'Q'">
      <QuestionItem :text="msg.text" />
    </div>
  </div>
</template>

<style scoped>
.chatHistory {
  display: inline-block;
  width: 60vw;
}
</style>
