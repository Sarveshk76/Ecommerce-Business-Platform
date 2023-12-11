export default defineNuxtRouteMiddleware((to, from) => {
    var token = "";
    if (process.client) {
        token = localStorage.getItem("token")??"";
    }

    if (token === "") {
        return to.path === "/login/customer" ? true : navigateTo("/login/customer");
    }else{
        return to.path === "/login/customer" ? navigateTo("/") : true;
    }
  });