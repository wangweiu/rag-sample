<script setup lang="ts">
import { MessageTwoTone } from '@ant-design/icons-vue'
defineProps({
  text: String,
})
</script>

<template>
  <div class="question">
    <MessageTwoTone />
    <!-- <UserOutlined /> -->
    <div class="userMsg">{{ text }}</div>
  </div>
</template>

<style scoped>
.userMsg {
  height: 2rem;
  line-height: 2rem;
  width: calc(100% - 50px);
  height: auto;
  display: inline-block;
  vertical-align: middle;
  margin-left: 10px;
}
.question {
  margin: 10px 0;
  * {
    vertical-align: middle;
  }
  >>> svg {
    width: 2em;
    height: 2rem;
  }
}
</style>
