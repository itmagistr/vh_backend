export default function currencyFormat(value, arg) {
  // return new Intl.NumberFormat("ru-ru").format(value);
  return new Intl.NumberFormat("ru-ru", {style: "currency", currency: arg, minimumFractionDigits: 0}).format(value);
}
