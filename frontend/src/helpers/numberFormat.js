export default function numberFormat(value) {
  return new Intl.NumberFormat("ru-ru").format(value);
  // return new Intl.NumberFormat("ru-ru", {style: "currency", currency: "RUB", minimumFractionDigits: 0}).format(value);
}
