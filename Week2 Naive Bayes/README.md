# 问题：性别分类
1. 训练样本：
<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;background:white;border-collapse:collapse;mso-yfti-tbllook:
 1184'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
  <td width="14%" style='width:14.48%;border:solid black 1.0pt;border-right:
  solid #A0A8AF 1.0pt;mso-border-alt:solid black .5pt;mso-border-right-alt:
  solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;mso-font-kerning:0pt;mso-no-proof:no'>Person<o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:solid black 1.0pt;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;
  mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:black;mso-border-left-alt:
  #A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:#A0A8AF;mso-border-style-alt:
  solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>height (feet)</span><span lang=EN-US style='font-size:16.0pt;font-family:
  "Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:0pt;
  mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:solid black 1.0pt;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;
  mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:black;mso-border-left-alt:
  #A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:#A0A8AF;mso-border-style-alt:
  solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>weight (<span class=SpellE>lbs</span>)</span><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border:solid black 1.0pt;border-left:none;
  mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>foot size(inches)</span><span lang=EN-US style='font-size:16.0pt;
  font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:
  0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1'>
  <td width="14%" style='width:14.48%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>male</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>6</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>180</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>12</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2'>
  <td width="14%" style='width:14.48%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>male</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>5.92 (5'11&quot;)</span><span lang=EN-US style='font-size:16.0pt;
  font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:
  0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>190</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>11</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3'>
  <td width="14%" style='width:14.48%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>male</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>5.58 (5'7&quot;)</span><span lang=EN-US style='font-size:16.0pt;
  font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:
  0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>170</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>12</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4'>
  <td width="14%" style='width:14.48%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>male</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>5.92 (5'11&quot;)</span><span lang=EN-US style='font-size:16.0pt;
  font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:
  0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>165</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>10</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5'>
  <td width="14%" style='width:14.48%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>female</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>5</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>100</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>6</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6'>
  <td width="14%" style='width:14.48%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>female</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>5.5 (5'6&quot;)</span><span lang=EN-US style='font-size:16.0pt;
  font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:
  0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>150</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>8</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7'>
  <td width="14%" style='width:14.48%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>female</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>5.42 (5'5&quot;)</span><span lang=EN-US style='font-size:16.0pt;
  font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:
  0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>130</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>7</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8;mso-yfti-lastrow:yes'>
  <td width="14%" style='width:14.48%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>female</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.74%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>5.75 (5'9&quot;)</span><span lang=EN-US style='font-size:16.0pt;
  font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:
  0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.18%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>150</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>9</span><span lang=EN-US style='font-size:16.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
</table>
2. 测试样本：
<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;background:white;border-collapse:collapse;mso-yfti-tbllook:
 1184'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
  <td width="14%" style='width:14.96%;border:solid black 1.0pt;border-right:
  solid #A0A8AF 1.0pt;mso-border-alt:solid black .5pt;mso-border-right-alt:
  solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;mso-font-kerning:0pt;mso-no-proof:no'>Person</span><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.6%;border-top:solid black 1.0pt;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;
  mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:black;mso-border-left-alt:
  #A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:#A0A8AF;mso-border-style-alt:
  solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>height (feet)</span><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:0pt;
  mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.04%;border-top:solid black 1.0pt;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;
  mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:black;mso-border-left-alt:
  #A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:#A0A8AF;mso-border-style-alt:
  solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>weight (<span class=SpellE>lbs</span>)</span><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.4%;border:solid black 1.0pt;border-left:none;
  mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>foot size(inches)</span><span lang=EN-US style='font-size:12.0pt;
  font-family:"Times New Roman",serif;mso-fareast-font-family:宋体;mso-font-kerning:
  0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;mso-yfti-lastrow:yes'>
  <td width="14%" style='width:14.96%;border-top:none;border-left:solid black 1.0pt;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-alt:solid black .5pt;mso-border-right-alt:solid #A0A8AF .5pt;
  padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>sample</span><span lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.6%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>6</span><span lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="25%" style='width:25.04%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid #A0A8AF 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-top-alt:
  black;mso-border-left-alt:#A0A8AF;mso-border-bottom-alt:black;mso-border-right-alt:
  #A0A8AF;mso-border-style-alt:solid;mso-border-width-alt:.5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>130</span><span lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
  <td width="34%" style='width:34.4%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid #A0A8AF .5pt;mso-border-alt:solid black .5pt;
  mso-border-left-alt:solid #A0A8AF .5pt;padding:.75pt .75pt .75pt .75pt'>
  <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
  auto;text-align:center;mso-pagination:widow-orphan'><span lang=EN-US
  style='font-size:16.0pt;font-family:"Times New Roman",serif;mso-fareast-font-family:
  宋体;color:black;mso-color-alt:windowtext;mso-font-kerning:0pt;mso-no-proof:
  no'>8</span><span lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman",serif;
  mso-fareast-font-family:宋体;mso-font-kerning:0pt;mso-no-proof:no'><o:p></o:p></span></p>
  </td>
 </tr>
</table>

# 解答：
### Import Packages
导包。
```
import numpy as np
from sklearn import model_selection
import scipy.stats as st
```
### Import dataset manually [Gender(0 for female, 1 for male) height(feet) weight(lbs) foot size(inches)]
首先手动输入数据，并转化成数组形式存放。
```
dataset = [
    [1, 6, 180, 12],
    [1, 5.92, 190, 11],
    [1, 5.58, 170, 12],
    [1, 5.92, 165, 10],
    [0, 5, 100, 6],
    [0, 5.5, 150, 8],
    [0, 5.42, 130, 7],
    [0, 5.75, 150, 9]
]
dataset = np.array(dataset)
```
### K-Fold
使用K折交叉验证对数据集进行随机划分，因为数据集内容较少，本次使用3折。
```
np.random.shuffle(dataset)
kf = model_selection.KFold(n_splits=3, shuffle=False)
for train_idx, test_idx in kf.split(dataset):
    data_train = dataset[train_idx]
    data_test = dataset[test_idx]
print(data_train)
```
得到训练集：<br>
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week2%20Naive%20Bayes/Output/Training%20Set.png)
### 函数1：将数组数据切分。
得到标签（target）与特征（feature）两个数组，以及数据数量、特征维度。
```
def divTarFea(arr):
    row = len(arr)
    col = len(arr[0]) - 1
    target = np.zeros(row)
    for i in range(row):
        target[i] = arr[i][0]
    feature = np.zeros([row, col])
    for i in range(row):
        for j in range(col):
            feature[i][j] = arr[i][j + 1]
    return row, col, target, feature
```

### 函数2：计算
得到先验概率、特征向量的均值（mean）和标准差（std）
```
def NaiveBayes(arr):
    # Dataset for Train Process
    data_num, feature_num, target, feature = divTarFea(arr)
    for i in range(data_num):
        for j in range(feature_num):
            feature[i][j] = arr[i][j + 1]
    # Number of Unique Target
    label = np.unique(target)
    label_num = label.size
    # Calculate Prior Probability
    prior = np.zeros(label_num)
    for i in range(label_num):
        temp = np.sum(target == label[i])
        prior[i] = temp / data_num
    # Calculate mean, standard deviation of features
    mean = np.zeros([label_num, feature_num])
    std = np.zeros([label_num, feature_num])
    for i in range(label_num):
        tmp_index = np.where(target == label[i])[0]
        for j in range(feature_num):
            tmp = np.zeros([1, len(tmp_index)])
            for k in range(len(tmp_index)):
                tmp[0][k] = feature[tmp_index[k]][j]
            mean[i][j] = np.mean(tmp)
            std[i][j] = np.std(tmp)
    return prior, mean, std, label_num
```
### 函数3：分类
根据得到的均值和标准差创建高斯分布，然后利用朴素贝叶斯进行分类。
```
def BayesClassification(feature, prior, mean, std, labelnum):
    row, col = feature.shape
    post = np.zeros([row, labelnum])
    estimate = np.zeros(row)
    for i in range(row):
        for j in range(labelnum):
            p_product = 1
            for k in range(col):
                p_product = p_product * st.norm.pdf(feature[i][k], mean[j][k], std[j][k])
            post[i][j] = p_product * prior[j]
        estimate[i] = np.argmax(post[i])
    return estimate
```
### 调用函数
```
prior, mean, std, label_num = NaiveBayes(data_train)
test_num, fea_num, label, score = divTarFea(data_test)
estmation = BayesClassification(score, prior, mean, std, label_num)
# Validation
right_num = estmation == label
rigth_rate = np.sum(right_num) / test_num
print('The accuracy is {:.2%}.'.format(rigth_rate))
```
因为对数据集进行了乱序处理后，再进行了K折交叉验证，所以每次分配的训练集和测试集内容不同，导致每次准确率的不同。
<br>
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week2%20Naive%20Bayes/Output/Accuracy.png)
### 估计
```
print("How many person you want to estimate?")
person = int(input())
data_user = np.zeros([person, fea_num])
print('Personal Data (feet weight footsize) and new line for another:')
for i in range(person):
    data_user[i] = input().split(" ")
result_user = BayesClassification(data_user, prior, mean, std, label_num)
for i in range(person):
    print('A person whose height is %.2f feet, weight is %.2f lbs, foot size is %.2f inches is inferred to be a'%(data_user[i][0], data_user[i][1], data_user[i][2]), end=" ")
    if result_user[i] == 0:
        print('female')
    else:
        print('male')
print(result_user)
```
使用测试样本与我自己的实际数据进行测试：<br>
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week2%20Naive%20Bayes/Output/Estimation.png)
