<template>
  <b-row>
    <b-col>
      <header>
        <h1>Passwords generator</h1>
        <p>See form below!</p>
      </header>
      <hr />
      <main>
        <b-row>
          <b-col cols="5">
            <form>
              <b-row>
                <b-col cols="6">
                  <label for="pass_len">Password length</label>
                </b-col>
                <b-col cols="6">
                  <input
                    id="pass_len"
                    v-model="options.length_"
                    type="number"
                    min="4"
                    max="60"
                  />
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <label for="pass_upper">Uppercase letters</label>
                </b-col>
                <b-col cols="6">
                  <input
                    id="pass_upper"
                    v-model="options.upper"
                    type="checkbox"
                  />
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <label for="pass_nums">Numbers</label>
                </b-col>
                <b-col cols="6">
                  <input
                    id="pass_nums"
                    v-model="options.nums"
                    type="checkbox"
                  />
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <label for="pass_special">Special characters</label>
                </b-col>
                <b-col cols="6">
                  <input
                    id="pass_special"
                    v-model="options.special"
                    type="checkbox"
                  />
                </b-col>
              </b-row>

              <hr />

              <b-row class="mb-2">
                <b-col cols="6">
                  <b-button @click="randomPassword">Randomize</b-button>
                </b-col>
                <b-col cols="6">
                  <label>
                    <input v-model="password" type="text" readonly />
                  </label>
                </b-col>
              </b-row>
            </form>
          </b-col>
        </b-row>
      </main>
    </b-col>
  </b-row>
</template>

<script>
export default {
  data() {
    return {
      options: {
        length_: 8,
        upper: false,
        nums: false,
        special: false,
      },
      password: ' ',
    }
  },
  methods: {
    data() {
      return {
        lower: 'abcdefghijklmnopqrstuvwxyz'.split(''),
        upper: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
        nums: '0123456789'.split(''),
        special: '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?'.split(''),
      }
    },
    randomPassword() {
      const data = this.data()
      const base = data.lower
      if (this.options.upper) base.push(...data.upper)
      if (this.options.nums) base.push(...data.nums)
      if (this.options.special) base.push(...data.special)
      let result = ''
      while (result.length <= this.options.length_) {
        result += base[Math.floor(Math.random() * base.length)]
      }
      this.password = result
    },
  },
}
</script>

<style></style>
