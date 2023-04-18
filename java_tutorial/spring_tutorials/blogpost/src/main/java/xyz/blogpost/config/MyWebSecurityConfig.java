package xyz.blogpost.config;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.security.SecurityProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.annotation.Order;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfiguration;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import xyz.blogpost.controller.UploadController;
import xyz.blogpost.service.CustomUserDetailsServiceImpl;

import javax.sql.DataSource;

@Configuration
@EnableWebSecurity
//@EnableGlobalMethodSecurity(prePostEnabled = true)
public class MyWebSecurityConfig extends WebSecurityConfigurerAdapter {

    private static final Logger logger = LoggerFactory.getLogger(MyWebSecurityConfig.class);
    @Autowired
    private DataSource dataSource;

    @Bean
    public UserDetailsService userDetailsService() {
        return new CustomUserDetailsServiceImpl();
    }

    @Bean
    public BCryptPasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }


    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.authenticationProvider(authenticationProvider());
    }

    @Bean
    public DaoAuthenticationProvider authenticationProvider() {
        DaoAuthenticationProvider authProvider = new DaoAuthenticationProvider();
        authProvider.setUserDetailsService(userDetailsService());
        authProvider.setPasswordEncoder(passwordEncoder());

        return authProvider;
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
                .authorizeRequests()
                .antMatchers("/", "/static/**", "/resources/**", "/css/**", "/js/**", "/register", "/process_register")
                .permitAll()
                .anyRequest().authenticated() // (4)
                .and()
                .formLogin() // (5)
                //.loginPage("/login") // (5)
                .permitAll()
                .and()
                .logout() // (6)
                .permitAll();
                //.and()
                //.httpBasic(); // (7)

//                .authorizeRequests((request) -> request
//                        .requestMatchers("/", "/index.html", "/static/**")).permitAll()
//                .anyRequest().authenticated()
//                .and()
//                .formLogin()
//                .loginPage("/login") // (1)
//                .permitAll();
    }

//    @Override
//    protected void configure(HttpSecurity http) throws Exception {  // (2)
//        http
//                .authorizeRequests()
//                .antMatchers("/", "/blogpost").permitAll() // (3)
//                .anyRequest().authenticated() // (4)
//                .and()
//                .formLogin() // (5)
//                .loginPage("/login") // (5)
//                .permitAll()
//                .and()
//                .logout() // (6)
//                .permitAll()
//                .and()
//                .httpBasic(); // (7)
//    }

//    @Override
//    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
//        auth.authenticationProvider(authenticationProvider());
//    }




//    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
//        http
//                .authorizeHttpRequests((requests) -> requests
//                        .antMatchers("/", "/register").permitAll()
//                        .anyRequest().authenticated()
//                )
//                .formLogin((form) -> form
//                        .loginPage("/register")
//                        .loginPage("/login")
//                        .permitAll()
//                )
//                .logout((logout) -> logout.permitAll());
//
//        return http.build();
//    }


//    @Override
    //protected void configure(HttpSecurity http) throws Exception {
//    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
//
//        logger.info("Hello http");
////        http.csrf().disable()
////                .authorizeRequests()
////                .antMatchers("/users").authenticated()
////                .anyRequest().permitAll()
////                .and()
////                .formLogin()
////                .usernameParameter("email")
////                //.defaultSuccessUrl("/users")
////                .defaultSuccessUrl("/")
////                .permitAll()
////                .and()
////                .logout().logoutSuccessUrl("/").permitAll();
//        http.csrf().disable()
//                .authorizeHttpRequests((requests) -> requests
//
//                                //.antMatchers("/blogpost")
////                        .requestMatchers("blogpost").permitAll()
//                        //.requestMatchers("/registration/**").permitAll()
//                        //.requestMatchers("/login/**").permitAll()
//                        //.requestMatchers("/user/**").hasAnyRole("USER", "ADMIN")
//                        //.requestMatchers("/admin/**").hasAnyRole("ADMIN")
//                                //.authenticated()
//                        .anyRequest().authenticated()
//                )
//                .formLogin((form) -> form
//                        .loginPage("/login")
//                        .loginProcessingUrl("/login")
//                        .loginProcessingUrl("/register")
//                        .defaultSuccessUrl("/user/")
//                        .permitAll()
//                )
//                .logout((logout) -> logout.permitAll())
//                .exceptionHandling().accessDeniedPage("/access-denied");
//        return http.build();
//    }

}
