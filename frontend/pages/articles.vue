<template>
    <section class="d-flex flex-column articles">
        <article v-for="post in data" :key="'post-' + post.id" class="blog-item d-flex row justify-content-center">
            <div class="col d-flex justify-content-center">
                <a :href="post.href">
                <img :src="post.img" alt="None">
                </a>
            </div>
            <div class="col">
                <h1><a :href="post.href">{{ post.title }}</a></h1>
                <p>
                    <span class="filters"> <template v-for="filter in post.filters">
                        <span v-if="filter.href == ''" :key="'filter-wo-' + filter.id">{{ filter.title }}</span>
                        <a v-else :key="'filter-' + filter.id" :href="filter.href">{{ filter.title }}</a>
                    </template> </span>
                     |  
                    <span class="authors"> <template v-for="author in post.authors">
                        <span v-if="author.href == ''" :key="'author-wo-' + author.id">{{ author.name }}</span>
                        <a v-else :href="author.href" :key="'author-' + author.id">{{ author.name }}</a>
                    </template> </span>
                </p>
                <p>{{ post.description }}</p>
                <div class="footer read-more"><a :href="post.href">читать далее »</a></div>
            </div>
        </article>
    </section>
</template>

<script>

export default {
//   filters: { currencyFormat, timeFormat },
  layout: 'def',
  props: {resize: Boolean},
  data() {
    return {
      data: [
        {id: 'post-bait-chew-sluggish-life-swim',
            title: 'Наживку жуёшь – вяло по жизни плывёшь',
            href: 'https://braginskyoleg.com/ru/content/2022/08/22/bait-chew-sluggish-life-swim/',
            img: 'https://braginskyoleg.com/braginskyoleg/media/filer_public_thumbnails/filer_public/f8/df/f8df2278-cbe8-46e6-becd-10f6bdfd5ce1/risunok1.jpg__450x300_q85_subsampling-2_upscale.jpg',
            description: 'Одурманенными косяками дрейфуем в прикормленные маркетологами рыбные места. Навязанные мысли заполняют голову: идеи щедрыми вёдрами заливаются через социальные сети, телевизор, глянец. Становится невыносимо больно отделять персональность от изнуряющего рекламного террора.',
            filters: [{id: 1, title: 'Мотивация', href: 'https://braginskyoleg.com/ru/calendars/treningi/t/561/?next=/ru/search/780a861e-0ec1-4659-b52a-1d05248c8b4f/'},
            {id: 2, title: 'Личная эффективность', href: 'https://braginskyoleg.com/ru/calendars/treningi/t/637/?next=/ru/search/560c05c9-acb7-4e79-bf00-6040f0fd9f25/'}],
            authors: [{id: 1, name: 'Олеся Дударь', href: ''}, 
            {id: 2, name: 'Даниил Шмитт', href: 'https://braginskyoleg.com/ru/teachers/2/'}]
        },
        {id: 'post-shamanism-troubleshooting',
            title: 'Шаманство траблшутера',
            href: 'https://braginskyoleg.com/ru/content/2022/08/10/shamanism-troubleshooting/',
            img: 'https://braginskyoleg.com/braginskyoleg/media/filer_public_thumbnails/filer_public/9a/9f/9a9fa745-1bd4-455a-833a-8818967e40ba/risunok_1.jpg__450x300_q85_subsampling-2_upscale.jpg',
            description: 'Какие ассоциации у вас вызывают слова шаманизм и траблшутинг? От обоих понятий веет непознанным и непостижимым. При погружении в тему находится много общего несмотря на диаметральную противоположность. Танцы с бубном – эзотерика, помощь бизнесу – материализм.',
            filters: [{id: 1, title: 'Траблшутинг', href: 'https://braginskyoleg.com/ru/calendars/treningi/t/189/?next=/ru/search/7d27ed67-2111-419c-83b2-17c6104ac026/'},
            {id: 2, title: 'Шаманизм', href: ''}],
            authors: [{id: 1, name: 'Альбина Анисимова', href: ''}, 
            {id: 2, name: 'Олег Брагинский', href: 'https://braginskyoleg.com/ru/teachers/1/'}]
        },
        {id: 'post-planning-business-value-growth',
            title: 'Планирование перспектив для повышения стоимости бизнеса',
            href: 'https://braginskyoleg.com/ru/content/2022/08/03/planning-business-value-growth/',
            img: 'https://braginskyoleg.com/braginskyoleg/media/filer_public_thumbnails/filer_public/cb/d5/cbd5b2f7-ab2b-4a07-8086-ca531e0ae2ef/risunok_1.jpg__450x300_q85_subsampling-2_upscale.jpg',
            description: 'Один из способов поднять стоимость кампании – сформировать планы дальнейшего успешного развития. Чем ярче представите картинку глазам потенциального покупателя, тем больше он будет готов раскошелиться.',
            filters: [{id: 1, title: 'Оценка бизнеса', href: 'https://braginskyoleg.com/ru/calendars/treningi/t/629/?next=/ru/search/7d782d93-da07-4689-b2d6-679ae71810fc/'},
            {id: 2, title: 'Финансы предеприятия', href: 'https://braginskyoleg.com/ru/calendars/treningi/t/13/?next=/ru/search/50f5c1a0-d039-4f4f-b93b-fafba120e981/'}],
            authors: [{id: 1, name: 'Владислав Чернов', href: ''}, 
            {id: 2, name: 'Олег Брагинский', href: 'https://braginskyoleg.com/ru/teachers/1/'}]
        },],
      locale: this.$i18n.locale,
    }
  },
  computed: { },
  watch: {
    "$i18n.locale": {
      handler(newLocale, oldLocale) {
        if (newLocale === oldLocale)
          return;
        this.locale = newLocale;
        // if (oldLocale !== undefined) { }
      },
      immediate: true
    },
  },
  beforeMount() {
    window.addEventListener('resize', this.checkSlider);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkSlider);
  },
  methods: { }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"
$minW: 769px

section.articles
  width: 100%
  margin: 2rem auto auto
  background-color: #f6f3edbf
  backdrop-filter: blur(2rem)
  border-radius: 1rem
  overflow: hidden
  > article.blog-item
    padding: 1rem
    border-bottom: 1px solid #836c26
    img
        max-width: 100%
        margin-right: .5rem
        border-radius: 0.75rem
    a 
        color: #836c26
        transition: all 0.3s ease-in-out
    > .col
        padding: 0
        span
            > span:not(:last-child)::after
                content: ', '
            > a:not(:last-child)::after
                content: ', '
  @media (min-width: 1400px)
    min-width: calc(100% - 248px)
    width: calc(100% - 248px)

@media (max-width: 992px)
    body.articles
        .container
            padding: 0
        section.articles
            margin: auto
            border-radius: 0
            > article
                flex-direction: column
                align-items: center
</style>
