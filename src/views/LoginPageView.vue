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
          <form action="">
            <div class="option">
              <img class="account" :src="imgSrc" alt="">
              <input class="input" type="text" placeholder="Account">
            </div>
            <div class="option">
              <i class="bi bi-lock-fill"></i>
              <input class="input" type="password" placeholder="Password">
            </div>
          </form>
          <button class="submit" type="submit">LOGIN</button>
          <p class="exception">Forget Username / Password</p>
          <div class="createAccount">
            <p class="exception">Create your Account</p>
            <i class="bi bi-arrow-right"></i>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import account from '../assets/pic/account.png'
export default {
  data() {
    return {
      imgSrc: account,
    };
  }
};
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
  margin: 0 0 80px 0;
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