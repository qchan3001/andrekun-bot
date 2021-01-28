from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
counter = 0
meigen = """「闘いのロマン」という引き出しこそ、もっとも開けて欲しいものなんだ。
アドバルーンを上げれば何かが動き出す。
もともとありもしない「限界」にこだわると、己れの力に疑問をもつようになり、しくじったり、できなかったとき、「ああ、これが俺の限界だ、もうダメだ」とギブアップしてしまう。
コンプレックスをバネに飛躍することができるのではないか。
落ちたら、またはいあがってくればいいだけのこと。
一生懸命やっている人を小馬鹿にするのは、自分がかなわないから笑うことで逃げているのだ。
どうってことはない。負けたと思ってないんだから。
しなやかな力はバランスがいい。
ちっちゃなケンカをするたびにスケールが小さくなる。
ただ単に相手を倒すだけであったのなら、社会において何の価値があろうか。
俺は人が喜んでくれるのが、生きがいというか喜び。
悩みながらたどり着いた結論は、やはりトレーニングしかない。
さあ、やるんだ。やり抜くのだ。
ルールを決めた以上はルール違反を犯さずに堂々と闘う。
姑息なことはするな！
人間には、必ず人生の転機を直感し、的確に判断できるかどうかを試される時が何度かある。
夢を持て！でかければでかいほどいい。とにかく、夢を持て。大ぶろしきをひろげておさまりがつかなくなってみろ、やらざるを得なくなるではないか。
元気が一番、元気があれば何でもできる！
自らに満足している人間は、それで終わりだ。
人は歩みを止めたときに、そして挑戦をあきらめたときに、年老いていくのだと思います。
わたしはプロレス修行時代、誰よりも大きな欲を持とうと思い練習した。
貧しいから手に入れようとするものがある。
ひとりだからこそできることもある。
踏み出せば、その一足が道となる。
道はどんなに険しくとも、笑いながら歩こうぜ！
子供に夢を持たせたければ、大人こそ夢を持て。
誰もが心底恐ろしい存在を持つべきだ。
長州は紙一重の差を破れなかった。
馬鹿になれ　とことん馬鹿になれ　恥をかけ　とことん恥をかけ　かいてかいて恥かいて　裸になったら見えてくる　本当の自分が見えてくる　本当の自分も笑ってた　それくらい　馬鹿になれ
死ぬエネルギーがあるくらいだったら、まだまだ生きられると思った。
自分の我を引っ込めたときには、必ずといっていいほど挫折感を味わう。
「迷わずいけよ」と言っても、俺にも迷う時もある。
裏切りというものもそれはそれでいいと思う。
力を抜くことによって、相手のエネルギーを奪うことができる。
心が歪むのは肉体自体が不健康だからだ。
優しさのない正義はなく、強さもない。
自分が受けた仕打ちを今度は自分がするというのは好きじゃない。
派手に見えれば見えるほど、裏で地味な努力をしているのがあらゆる世界のプロだ。
出る前に負けること考えるバカいるかよ!
リングに上がっているのに、なぜスキを見せるのか。
常識から1ミリでもいいから一歩踏み出せ。
別れる時にはもう次の恋が始まっている。
最終的に相手を認めていく。
""".splitlines()



@bot.event
async def on_message(message):
   if bot.user in message.mentions:
      if random.random() < 0.25:
        reply = f'{message.author.mention} {meigen[random.randint(0, 42)]}'
      else:
        reply = f'{message.author.mention} なんだバカヤロー'
      await message.channel.send(reply)
   global counter
   if message.content == "1":
        counter = 1
        await message.channel.send("2!!")
   if message.content == "3" and counter == 1:
        counter = 0
        reply = f'{meigen[random.randint(0, 42)]}'
        await message.channel.send('ダーーーーーーー！！！！！！！！！！！\n' + reply)
   if message.content == "猪木" or message.content == "イノキ" or message.content == "いのき":
        await message.channel.send('ボンバイエ!')
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
