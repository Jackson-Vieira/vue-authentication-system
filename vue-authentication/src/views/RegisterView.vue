<template>
  <form class="form-signin" @submit.prevent="submit">
    <h1 class="h3 mb-3 font-weight-normal">Please register</h1>
    <input
      class="form-control"
      placeholder="Username"
      required
      v-model="data.username"
    />
    <input
      type="email"
      class="form-control"
      placeholder="Email address"
      required
      v-model="data.email"
    />
    <input
      type="password"
      class="form-control"
      placeholder="Password"
      required
      v-model="data.password"
    />
    <button class="btn btn-lg btn-primary btn-block" type="submit">
      Submit
    </button>
  </form>
</template>

<script lang="ts">
import { reactive } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "RegisterView",
  setup() {
    const data = reactive({
      username: "",
      email: "",
      password: "",
    });

    const router = useRouter();


    const submit = async () => {
      await fetch("http://localhost:8000/api/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          
        },
        body: JSON.stringify(data),
      });

      await router.push('/signin')
    };

    return {
      data,
      submit,
    };
  },
};
</script>

<style scoped></style>
