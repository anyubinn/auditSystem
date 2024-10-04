function updateDateTime() {
  const currentDateElement = document.getElementById("current-date");

  const now = new Date();
  const options = { weekday: 'long', month: 'short', day: 'numeric', timeZone: 'Asia/Seoul' };
  // year: 'numeric', 
  
  const formattedDate = now.toLocaleDateString('en-KR', options).toUpperCase();


  currentDateElement.textContent = formattedDate.replace(/, /, '\n');
  

}

    
// Update date and time every second
setInterval(updateDateTime, 1000);

// Initial call to display date and time
updateDateTime();



// 이거는 차트 만드는 부분임.
document.addEventListener('DOMContentLoaded', () => {
  const numericValues = value.map(item => parseInt(item, 10));
  const totalValue = numericValues.reduce((sum, item) => sum + item, 0)
  const percentageGreen = numericValues[0] / totalValue;
  const percentageYellow = numericValues[1] / totalValue;
  const percentageRed = numericValues[2] / totalValue;
  console.log(percentageGreen);
  const data = [
    { label: 'CategoryGreen', value: percentageGreen, color: '#00BF63' },
    { label: 'CategoryYellow', value: percentageYellow, color: '#FFDE59' },
    { label: 'CategoryRed', value: percentageRed, color: '#FF3131' },
  ];

  const canvas = document.getElementById('donutChart');
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const outerRadius = Math.min(centerX, centerY) - 50; //차트 크기 조정
  const innerRadius = outerRadius * 0.6;

  let startAngle = -Math.PI / 2;

  data.forEach(item => {
    const percentage = ((item.value) * 100).toFixed(1);
    const sliceAngle = (item.value) * 2 * Math.PI;

    // Outer arc
    ctx.beginPath();
    ctx.arc(centerX, centerY, outerRadius, startAngle, startAngle + sliceAngle);
    ctx.lineTo(centerX, centerY);
    ctx.fillStyle = item.color;
    ctx.fill();

    // Inner arc
    ctx.beginPath();
    ctx.arc(centerX, centerY, innerRadius, startAngle + sliceAngle, startAngle, true);
    ctx.lineTo(centerX, centerY);
    ctx.fillStyle = '#473DC6';  // Set inner color to background color
    ctx.fill();

    // Display percentage outside the chart
    const labelX = centerX + (outerRadius + 30) * Math.cos(startAngle + sliceAngle / 2);
    const labelY = centerY + (outerRadius + 30) * Math.sin(startAngle + sliceAngle / 2);
    ctx.fillStyle = 'white';
    ctx.font = '20px Arial';
    ctx.textAlign = 'center';
    ctx.fillText(`${percentage}%`, labelX, labelY);

    startAngle += sliceAngle;
  });
});


