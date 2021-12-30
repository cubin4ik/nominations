function expand () {
    console.log('buttonclicked')
    elements = document.querySelectorAll('.expand')
    for (const item of elements) {
        item.classList.toggle('hidden')
    }
}