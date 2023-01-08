<template>
  <form class="form-signin" @submit.prevent="submit">
    <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
    <input
      class="form-control"
      placeholder="Username"
      required
      autofocus
      v-model="data.username"
    />
    <input
      type="password"
      id="inputPassword"
      class="form-control"
      placeholder="Password"
      required
      v-model="data.password"

    />
    <button class="btn btn-lg btn-primary btn-block" type="submit">
      Sign in
    </button>
  </form>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "LoginView",
  setup() {
    const data = reactive({
      username: "",
      password: "",
    });

    const router = useRouter();

    const submit = async () => {
      const res = await fetch("http://localhost:8000/api/token/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify(data),
      });

      const fetchData =  await res.json();
      
      // Cookie is better :) but
      localStorage.setItem('accesstoken', fetchData.access);


      await router.push('/')
    };

    return {
      data, 
      submit
    }
  },
});
</script>

<style scoped></style>
