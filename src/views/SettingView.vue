<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex justify-content-center align-items-center w-100">
      <div class="outer">
        <form action="">
          <label for="">Email</label>
          <input type="email">
          <label for="">Password</label>
          <input type="password">
          <label for="">Authority</label>
          <input type="text">
        </form>
        <div class="submit">
          <button class="store">
            <img id="store" src="../assets/pic/store.png" alt="" style="width: 30px; height: 35px;">
            <p>store</p>
          </button>
          <button class="reset">
            <img id="reset" src="../assets/pic/reset.png" alt="" style="width: 35px; height: 35px;">
            <p>reset</p>
          </button>
        </div>
        <button class="logout">
          <img id="logout" src="../assets/pic/logout.png" alt="" style="width: 35px; height: 35px;">
          <p>logout</p>
        </button>

      </div>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
import $ from 'jquery'
import store from '../assets/pic/store.png'
import store_blue from '../assets/pic/store_blue.png'
import reset from '../assets/pic/reset.png'
import reset_blue from '../assets/pic/reset_blue.png'
import logout from '../assets/pic/logout.png'
import logout_blue from '../assets/pic/logout_blue.png'

export default {
  components: {
    MenuBar
  },
  mounted() {
    $(document).ready(function () {
      $('.store').hover(function () {
        $(this).find('img').attr("src", store_blue);
        $(this).find('p').show();
      }, function () {
        $(this).find('img').attr("src", store);
        $(this).find('p').hide();
      });
      $('.reset').hover(function () {
        $(this).find('img').attr("src", reset_blue);
        $(this).find('p').show();
      }, function () {
        $(this).find('img').attr("src", reset);
        $(this).find('p').hide();
      });
      $('.logout').hover(function () {
        $(this).find('img').attr("src", logout_blue);
        $(this).find('p').show();
      }, function () {
        $(this).find('img').attr("src", logout);
        $(this).find('p').hide();
      });
    });
  }
}
</script>

<style scoped>
.outer {
  background-color: #222222;
  width: 75vw;
  height: 60vh;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}


input {
  background-color: #3A3A3A;
  border: 2px solid #868686;
  border-radius: 10px;
  padding: 0 10px 0 10px;
  color: #FFFFFF;
  outline: none;
}

label {
  color: #FFFFFF;
}

form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.submit {
  position: absolute;
  bottom: 20px;
  display: flex;

}

.logout {
  position: absolute;
  right: 10px;
  top: 10px;
  display: flex;
  align-items: flex-end;
  border-bottom: 1px solid transparent;
  transition: 300ms all ease;
  color: #868686;
  background-color: transparent;
  border: none;
  border-bottom: 1px solid transparent;
}

.logout:hover {
  border-color: #868686;
}

.store {
  display: flex;
  align-items: flex-end;
  transition: 300ms all ease;
  color: #868686;
  margin: 0 10px 0 0;
  background-color: transparent;
  border: none;
  border-bottom: 1px solid transparent;
}

.store:hover {
  border-color: #868686;
}

.reset {
  display: flex;
  align-items: flex-end;
  border-bottom: 1px solid transparent;
  transition: 300ms all ease;
  color: #868686;
  background-color: transparent;
  border: none;
  border-bottom: 1px solid transparent;
}

.reset:hover {
  border-color: #868686;
}

p {
  color: aliceblue;
  margin: 0 5px 0 5px;
  display: none;
}
</style>