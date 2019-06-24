CREATE TABLE `kr` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `article_id` int(11) DEFAULT NULL COMMENT '文章ID',
  `article_title` varchar(500) DEFAULT NULL COMMENT '标题',
  `column_name` varchar(100) DEFAULT NULL COMMENT '类别',
  `column_id` int(11) DEFAULT NULL COMMENT '类别ID',
  `cover` varchar(500) DEFAULT NULL COMMENT '封面图片链接',
  `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
  `summary` varchar(1000) DEFAULT NULL COMMENT '文章总结',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1241 DEFAULT CHARSET=utf8mb4