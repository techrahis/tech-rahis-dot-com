module.exports = {
  content: ["./**/templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        opensans: ["Open Sans", "sans-serif"],
        montserrat: ["Montserrat", "sans-serif"],
        inter: ["Inter", "sans-serif"],
        "press-start": ['"Press Start 2P"', "system-ui"],
      },
      screens: {
        xs: "320px",
        sm: "640px",
        md: "768px",
        lg: "1024px",
        xl: "1280px",
        "2xl": "1536px",
      },
      animation: {
        "spin-clock": "spin 6s linear infinite",
        "ping-status": "ping 1s ease-in-out infinite",
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
