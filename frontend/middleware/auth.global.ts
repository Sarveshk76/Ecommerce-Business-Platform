export default defineNuxtRouteMiddleware((to, from) => {
    var token = "";
    if (process.client) {
        token = localStorage.getItem("token")??"";
    }

    if (token === "") {
        return to.path === "/login/customer" ? true : navigateTo("/login/customer") || 
        to.path === "/login/register" ? true : navigateTo("/login/register");
    }else{
        return to.path === "/login/customer" ? navigateTo("/") : true;
    }
  });