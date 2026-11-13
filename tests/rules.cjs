const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(require('path').join(__dirname,'../index.html'),'utf8');
const js=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)][0][1];
let offset=0;const context={URLSearchParams,location:{search:'?test=1'},localStorage:{getItem:()=>null,setItem:()=>{}},sessionStorage:{getItem:()=>String(offset),setItem:(_,v)=>offset=Number(v)},Date};vm.createContext(context);vm.runInContext(js,context);
const evaljs=s=>vm.runInContext(s,context);
function day(i){evaljs(`setOffset(dayOneOffset()+${i})`)}
function record(n){evaljs(`state.days[keyOf(today())]={pedal:${n>=1},exercises:${n>=2},walk:${n===3}}`)}
function reset(){evaljs('state={days:{},celebrated:{},unlockDay:{}}')}
reset();let quotes=[];
for(let i=0;i<56;i++){day(i);quotes.push(evaljs('QUOTES[Math.max(0,Math.min(TOTAL_DAYS-1,dayIndex()))][0]'));}
assert.equal(new Set(quotes).size,56);console.log('PASS: 56 distinct daily quotes selected across 56 simulated days');
reset();for(let i=0;i<7;i++){day(i);record(2);let s=evaljs('badgeStates()');assert.equal(s.first,true);assert.equal(s.s2,i>=1);assert.equal(s.s3,i>=2);assert.equal(s.s7,i>=6);assert.equal(s.weekly,i>=2)}console.log('PASS: first-day, 2/3/7-day streak and weekly badge thresholds');
reset();for(let i=0;i<28;i++){day(i);record(i%7<3?2:0);assert.equal(evaljs('championEarned()'),i>=23)}console.log('PASS: four consecutive program weeks with three good days unlock Champion on day 24');
reset();for(let i=0;i<35;i++){day(i);record(Math.floor(i/7)!==2 && i%7<3?2:0)}assert.equal(evaljs('championEarned()'),false);console.log('PASS: missed weekly star breaks Champion sequence');
reset();day(55);assert.equal(evaljs('badgeStates().done'),false);record(2);assert.equal(evaljs('badgeStates().done'),true);day(54);assert.equal(evaljs('badgeStates().done'),false);assert.equal(evaljs('streakDayTotal()'),0);console.log('PASS: completion requires January 4 and participation; future records excluded');
