// manage blood group selection
let blood_grp_btn = document.querySelectorAll('div.blood-grp');

blood_grp_btn.forEach(btn => {
    btn.addEventListener('click', () =>{
        let url = btn.dataset.url;
        window.open(url,'_self');
    });
});