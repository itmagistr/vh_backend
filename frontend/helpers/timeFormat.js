export default function timeFormat(value, arg) {
  switch(arg) {
    case "ru-RU": return value + " мин";
    case "en-EN": return value + " min"
    default: return value + " мин";
  }
}
