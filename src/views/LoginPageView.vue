<template>
  <div class="bgLogin">
    <div class="container">
      <div class="row">
        <div class="col-5 profile">
          <div class="circle">
            <div class="rec_gray">
              <i class="bi bi-person-circle"></i>
            </div>
          </div>
        </div>
        <div class="col-5 info">
          <h2 class="title">XXXX館</h2>
          <h1 class="subtitle">Member Login</h1>
          <div class="hasUser" v-if="this.$store.state.currentUser != ''">
            目前有人使用，請稍後 ...
          </div>
          <div class="noUser" v-else>
            目前無人使用，歡迎您
          </div>
          <form @submit.prevent="memberLogin" class="d-flex flex-column align-items-center">
            <div class="option">
              <img class="account" :src="imgSrc" alt="">
              <input name="Account" class="input" type="text" placeholder="Account" v-model="loginForm.account">
            </div>
            <div class="option">
              <i class="bi bi-lock-fill"></i>
              <input name="Password" class="input" type="password" placeholder="Password" v-model="loginForm.password">
            </div>

            <button class="submit" type="submit">LOGIN</button>

            <!-- <p class="exception">If you forget Username / Password, call us</p>
            <div class="createAccount">
              <p class="exception">Create your Account</p>
              <i class="bi bi-arrow-right"></i>
            </div> -->
          </form>
          <div v-if="loginStatus == 'Failed'" class="d-flex justify-content-center align-items-center"
            style="font-weight: 800">
            <img :src="errorSrc" style="width: 40px; height: 40px">
            帳號或密碼不存在
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
// import Cookies from 'js-cookie'
import axios from 'axios';
import { defineComponent } from "vue";

import account from '../assets/pic/account.png'
import error from '../assets/pic/loginerror.png'

export default defineComponent({
  setup() {

  },
  data() {
    return {
      imgSrc: account,
      errorSrc: error,
      loginForm: {
        account: '',
        password: '',
        token: ''
      },
      loginStatus: false,
    };
  },
  methods: {
    async memberLogin() {
      let useraccount = this.loginForm.account
      let userpassword = this.loginForm.password

      this.$store.state.currentUser = useraccount  //記錄誰現在正在系統內部

      await axios({
        method: 'post',
        url: this.$store.state.api + '/login',
        headers: {
          accept: 'application/json',
          'Content-Type': 'multipart/form-data'
          // 'Authorization': `Bearer ${token}` // Bearer 跟 token 中間有一個空格
        },
        data: {
          'Account': useraccount,
          'Password': userpassword
        }
      }).then(response => {
        this.loginStatus = response.data
        console.log(this.loginStatus)
        if (this.loginStatus == 'Success') {
          this.$router.push({ name: 'home' })
        }
        else {
          return response.data;
        }

      }).catch(err => {
        console.log(err);
      })
    }
  }
});
</script>


<style scoped>
.bgLogin {
  background-color: #494949;
  display: flex;
  height: 100vh;
  align-items: center;
}

.bgLogin .container {
  background-color: #FFFFFF;
  width: 1400px;
  height: 700px;
  display: flex;
  border-radius: 20px;
}

.noUser {
  background-color: rgba(0, 0, 0, 0.1);
  width: 250px;
  height: 40px;
  border-radius: 5px;
  text-align: center;
  color: #00c853;
  margin: 25px 0px;
  font-weight: bold;
  font-size: 20px;
  line-height: 2;
  box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.5);
}

.hasUser {
  background-color: rgba(0, 0, 0, 0.1);
  width: 250px;
  height: 40px;
  border-radius: 5px;
  text-align: center;
  color: #d50000;
  margin: 25px 0px;
  font-weight: bold;
  font-size: 20px;
  line-height: 2;
  box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.5);
}

.row {
  width: 100%;
  justify-content: center;
  padding: 0;
  margin: 0 auto;
}

.circle {
  background-color: #D9D9D9;
  width: 400px;
  height: 400px;
  border-radius: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.rec_gray {
  background-color: #6F6F6F;
  width: 280px;
  height: 180px;
  border: 10px solid #353535;
  display: flex;
  justify-content: center;
  align-items: center;
}

.bi-person-circle {
  font-size: 90px;
  color: #DDDDDD;
}

.container .profile {
  align-self: center;
  display: flex;
  justify-content: center;
}

.container .info {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 700px;

}

.title {
  font-weight: bold;
  margin: 80px 0 30px 0;
}

.subtitle {
  font-weight: bold;
  margin: 0 auto;
}

.option {
  display: flex;
  align-items: center;
  background-color: #D9D9D9;
  border-radius: 50px;
  width: 300px;
  height: 50px;
  justify-content: center;
  margin-bottom: 15px;
}

.account {
  width: 35px;
  margin-right: 20px;
}

.bi-lock-fill {
  font-size: 30px;
  color: #353535;
  margin-right: 20px;
}

.input {
  background-color: #D9D9D9;
  border: none;
  outline: none;
}

.submit {
  display: block;
  background-color: #54BB15;
  border-radius: 50px;
  width: 320px;
  height: 60px;
  font-weight: bolder;
  color: #FFFFFF;
  font-size: 24px;
  margin: 20px 0 15px 0;
  border: none;
}

.submit:hover {
  background-color: #4da814;
}

.exception {
  border-bottom: 1px solid transparent;
  transition: 500ms all ease;
  color: #868686;
  margin: 0;
}

.exception:hover {
  border-color: #868686;
}

.createAccount {
  display: flex;
  align-items: center;
  margin-top: 140px;
}
</style>