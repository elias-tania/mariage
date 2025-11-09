<template>
  <div class="combobox">
    <input
      type="text"
      class="combobox-input"
      :placeholder="placeholder"
      v-model="search"
      @focus="open = true"
      @input="onInput"
      @blur="closeWithDelay"
      @keydown.down.prevent="moveDown"
      @keydown.up.prevent="moveUp"
      @keydown.enter.prevent="selectHighlighted"
    />

    <ul v-if="open && filteredOptions.length" class="combobox-list">
      <li
        v-for="(option, index) in filteredOptions"
        :key="option"
        :class="['combobox-item', { active: index === highlightedIndex }]"
        @mousedown.prevent="select(option)"
      >
        {{ option }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ComboBox",
  props: {
    modelValue: String,
    options: {
      type: Array,
      default: () => []
    },
    placeholder: {
      type: String,
      default: ""
    }
  },
  emits: ["update:modelValue"],
  data() {
    return {
      search: this.modelValue || "",
      open: false,
      highlightedIndex: -1
    }
  },
  computed: {
    filteredOptions() {
      const term = this.search.toLowerCase()
      return this.options.filter(o => o.toLowerCase().includes(term))
    }
  },
  watch: {
    modelValue(newVal) {
      this.search = newVal
    }
  },
  methods: {
    onInput() {
      this.$emit("update:modelValue", this.search)
      this.open = true
      this.highlightedIndex = -1
    },
    select(option) {
      this.search = option
      this.$emit("update:modelValue", option)
      this.open = false
    },
    moveDown() {
      if (!this.open) this.open = true
      if (this.highlightedIndex < this.filteredOptions.length - 1) {
        this.highlightedIndex++
      }
    },
    moveUp() {
      if (this.highlightedIndex > 0) {
        this.highlightedIndex--
      }
    },
    selectHighlighted() {
      if (this.highlightedIndex >= 0) {
        this.select(this.filteredOptions[this.highlightedIndex])
      } else {
        this.open = false
      }
    },
    closeWithDelay() {
      setTimeout(() => (this.open = false), 100)
    }
  }
}
</script>

<style scoped>
.combobox {
  position: relative;
  width: 100%;
  box-sizing: border-box;

}

.combobox-input {

  border: 1px solid #ccc;
  border-radius: 0.4em;
  font-size: 1rem;
  box-sizing: border-box !important;
  width: 100%;

}

.combobox-list {
  position: absolute;
  z-index: 10;
  background: white;
  border: 1px solid #ccc;
  border-top: none;
  width: 100%;
  max-height: 180px;
  overflow-y: auto;
  list-style: none;
  margin: 0;
  padding: 0;
}

.combobox-item {
  padding: 0.5em;
  cursor: pointer;
}

.combobox-item:hover,
.combobox-item.active {
  background-color: #f0f0f0;
}
</style>
