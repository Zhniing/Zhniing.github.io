require 'time'

# cnt = 0

Jekyll::Hooks.register :posts, :pre_render do |post|
    # cnt = cnt + 1
    # puts "123456789 #{post.path}  #{File.extname(post.path)} cnt=#{cnt}"

    # get the current post last modified time
    # modification_time = File.mtime( post.path )
    modification_timestamp = `git log -1 --format="%ct" "#{post.path}"`
    
    # puts "#{post.path} #{modification_timestamp}"

    # inject modification_time in post's datas.
    post.data['last-modified-date'] = Time.at Integer(modification_timestamp)

end