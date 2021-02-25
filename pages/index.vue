<template>
  <b-row class="my-4">
    <b-col>
      <header>
        <h1>Passwords generator</h1>
        <p>See form below!</p>
      </header>
      <hr />
      <main>
        <b-row>
          <b-col cols="5">
            <b-form-group label="Password length test">
              <b-form-input
                v-model.number="options.length_"
                type="number"
                min="4"
                max="60"
                required
              />
            </b-form-group>

            <b-form-group label="Use uppercase letters">
              <input v-model="options.upper" type="checkbox" />
              <span>
                {{ options.upper ? 'Yes' : 'No' }}
              </span>
            </b-form-group>

            <b-form-group label="Use numbers">
              <input v-model="options.nums" type="checkbox" />
              <span>
                {{ options.nums ? 'Yes' : 'No' }}
              </span>
            </b-form-group>

            <b-form-group label="Use special characters">
              <input
                id="pass_special"
                v-model="options.special"
                type="checkbox"
              />
              <span>
                {{ options.special ? 'Yes' : 'No' }}
              </span>
            </b-form-group>

            <hr />

            <b-row class="mb-2">
              <b-col cols="6">
                <b-button
                  variant="primary"
                  class="w-100"
                  @click="randomPassword"
                >
                  Randomize
                </b-button>
              </b-col>
              <b-col cols="6">
                <b-form-group
                  :description="
                    password === ' '
                      ? 'Here will be displayed generated password.'
                      : 'See? Great!'
                  "
                >
                  <b-form-input v-model="password" type="text" readonly />
                </b-form-group>
              </b-col>
            </b-row>
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
