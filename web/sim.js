// 华雄模拟核心逻辑（与Python实现一致）
function simulateHuaxiong(initialHuaxiong, killTime, cureTime) {
    let alive = initialHuaxiong;
    let dead = 0;
    let time = 0;
    let killCount = 0;
    let guanyv = 0, guanyvTime = 0;
    let huatuo = 0, huatuoTime = 0;

    function guanyv_kill() {
        if (guanyv === 1 && time - guanyvTime >= killTime) {
            alive -= 1;
            dead += 1;
            killCount += 1;
            guanyv = 0;
        }
        if (alive > 0 && guanyv === 0) {
            guanyv = 1;
            guanyvTime = time;
        }
    }

    function huatuo_cure() {
        if (huatuo === 1 && time - huatuoTime >= cureTime) {
            alive += 1;
            dead -= 1;
            huatuo = 0;
        }
        if (dead > 0 && huatuo === 0) {
            huatuo = 1;
            huatuoTime = time;
        }
    }

    while (alive > 0) {
        guanyv_kill();
        huatuo_cure();
        guanyv_kill(); // 关羽可能在同一时间砍两只华雄
        if (alive === 0) break;
        time += 1;
    }
    return { killCount, time };
}

// 绑定表单事件
const form = document.getElementById('simForm');
const resultDiv = document.getElementById('result');
form.onsubmit = function(e) {
    e.preventDefault();
    const n = parseInt(document.getElementById('huaxiong').value, 10);
    const killTime = parseInt(document.getElementById('killTime').value, 10);
    const cureTime = parseInt(document.getElementById('cureTime').value, 10);
    if (isNaN(n) || n < 1 || isNaN(killTime) || killTime < 1 || isNaN(cureTime) || cureTime < 1) {
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = '请输入有效的参数！';
        return;
    }
    const res = simulateHuaxiong(n, killTime, cureTime);
    resultDiv.style.display = 'block';
    // 输出华雄图片（huaxiong.png）
    resultDiv.innerHTML = `您共杀死了<b>${res.killCount}</b>只华雄！<br>总耗时：<b>${res.time}</b>s<br><img src="huaxiong.png" alt="华雄Q版" class="huaxiong-img">`;
};
